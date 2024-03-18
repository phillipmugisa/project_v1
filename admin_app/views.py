from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
import decimal
from django.http import FileResponse
import os

from django.conf import settings
from django.core.mail import send_mail

from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from manager import models as ManagerModels
from clinicMas import models as ClinicModels
from manager import forms as ManagerForms
from admin_app.mixins import AdminAndAuthenticatedAccessMixin

import random

def group_instances(insurances):
    insurance_groups = []
    for insurance in insurances:
        # get insurance beneficians
        beneficians = ManagerModels.FamilyMember.objects.filter(family=insurance.family, status=True)

        data = {
            "insurance": insurance,
            "benefician_count": len(beneficians)
        }
        insurance_groups.append(data)
    return insurance_groups

def group_patients(patients):
    patient_groups = []
    
    for patient in patients:
        family = None
        family_status = None
        insurance_type = None
        access_type=None
        families = ManagerModels.FamilyMember.objects.filter(patient__patientno=patient.patientno)
        if families:
            family = families.first().family
            family_status = families.first().status
            insurance_type = families.first().relationship
            access_type = families.first().access_type

        data = {
            "patient" : patient,
            "family": family,
            "insurance_status": family_status,
            'insurance_type': insurance_type,
            'access_type': access_type
        }
        patient_groups.append(data)

    return patient_groups

def generate_insurance_no(family_name):
    insurance_no = f"{random.randint(0,10)}{random.randint(0,10)}{random.randint(0,10)}"
    return insurance_no

class AdminHomeView(AdminAndAuthenticatedAccessMixin, View):
    template_name = "admin_app/home.html"
    template_partial_insurance_name = "admin_app/partials/__insurance_list.html"
    template_partial_patient_name = "admin_app/partials/__patient_list.html"
    context_data = {}

    def get(self, request):
        insurances = ManagerModels.FamilyInsurance.objects.all()
        self.context_data["insurances"] = group_instances(insurances)

        if request.htmx:
            return render(request, template_name=self.template_partial_insurance_name, context=self.context_data)
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):

        # for insurance data
        insurance_data = request.POST.get("insurance_data")
        if insurance_data:
            insurances = ManagerModels.FamilyInsurance.objects.filter(Q(insurance_number = insurance_data) | Q(family__name__iexact = insurance_data))

            if not insurances:
                messages.add_message(request, messages.ERROR, _("Invalid Family name or Insurance Number"))

            self.context_data["insurances"] = group_instances(insurances)
            if request.htmx:
                return render(request, template_name=self.template_partial_insurance_name, context=self.context_data)
            return render(request, template_name=self.template_name, context=self.context_data)


        # patient data
        patient_data = request.POST.get("patient_data")
        if patient_data:
            patient_data = patient_data.strip()
            
            if len(patient_data.split(" ")) == 2:
                name = patient_data.split(" ")
                patients = ClinicModels.Patients.objects.using("clinic").filter(Q(firstname__icontains=name[0], lastname__icontains=name[1]) | Q(firstname__icontains=name[1], lastname__icontains=name[0]))
            else:
                patients = ClinicModels.Patients.objects.using("clinic").filter(Q(patientid__icontains=patient_data) | Q(patientno__icontains=patient_data) | Q(nationalidno__icontains=patient_data) | Q(referenceno__icontains=patient_data) | Q(firstname__icontains=patient_data) | Q(lastname__icontains=patient_data) | Q(middlename__icontains=patient_data))
            
            if not patients:
                messages.add_message(request, messages.ERROR, _("Invalid Patient Data"))
            
            self.context_data["patients"] = group_patients(patients)
            return render(request, template_name=self.template_partial_patient_name, context=self.context_data)

        
        family_name = request.POST.get("family_name")
        if family_name:
            family_name = family_name.strip()
            family = ManagerModels.Family(name=family_name)
            family.save()

            # create insurance
            family_insurance = ManagerModels.FamilyInsurance(insurance_number=generate_insurance_no(family_name),family=family,credit=0, status=False)
            family_insurance.save()
            return redirect(reverse("admin_app:home"))

        return redirect(reverse("admin_app:home"))

def modifyInsuranceStatusView(request, insurance_number):
    if request.method == "POST":
        insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance_number)

        if not insurances:
            messages.add_message(request, messages.ERROR, _("Invalid Family name or Insurance Number"))
            return redirect(reverse("admin_app:home"))

        insurance = insurances.first()
        if request.POST.get("suspend"):
            insurance.status = False
        elif request.POST.get("activate"):
            insurance.status = True

        insurance.save()
        return redirect(reverse("admin_app:home"))
        
    messages.add_message(request, messages.ERROR, _("Method not allowed."))
    return redirect(reverse("admin_app:home"))



class AdminInsuranceDetialView(AdminAndAuthenticatedAccessMixin, View):
    template_name = "admin_app/insurance_details.html"
    template_partial_insurance_name = "admin_app/partials/__insurance_list.html"
    template_partial_patient_name = "admin_app/partials/__patient_list.html"
    context_data = {}

    def get(self, request, insurance_number):
        insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance_number)

        if not insurances:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:home"))

        insurance = insurances.first()
        self.context_data["insurance"] = insurance

        
        self.context_data["benefician_count"] = group_instances(insurances)[0]["benefician_count"]
        
        # get family members by family name (lastname)
        family_members = ManagerModels.FamilyMember.objects.filter(family=insurance.family)
        self.context_data["family_members"] = family_members
        
        patients = []
        for fm in family_members:
            patients.append(fm.patient)

        self.context_data["patients"] = group_patients(patients)

        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request, insurance_number):

        if request.POST.get("toggle_status"):
            # change insurance status
            insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance_number)

            if not insurances:
                messages.add_message(request, messages.ERROR, _("Record not found."))
                return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

            insurance = insurances.first()
            insurance.status = not insurance.status
            insurance.save()
            return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

        # patient data
        self.context_data["patients"] = []
        patient_data = request.POST.get("patient_data")
        if patient_data:
            patient_data = patient_data.strip()
            
            if len(patient_data.split(" ")) == 2:
                name = patient_data.split(" ")
                patients = ClinicModels.Patients.objects.using("clinic").filter(Q(firstname__icontains=name[0], lastname__icontains=name[1]) | Q(firstname__icontains=name[1], lastname__icontains=name[0]))
            else:
                patients = ClinicModels.Patients.objects.using("clinic").filter(Q(patientid__icontains=patient_data) | Q(patientno__icontains=patient_data) | Q(nationalidno__icontains=patient_data) | Q(referenceno__icontains=patient_data) | Q(firstname__icontains=patient_data) | Q(lastname__icontains=patient_data) | Q(middlename__icontains=patient_data))
            
            if not patients:
                messages.add_message(request, messages.ERROR, _("Invalid Patient Data"))
            
            self.context_data["patients"] = group_patients(patients)
            
        return render(request, template_name=self.template_partial_patient_name, context=self.context_data)

def assignPatienttoFamily(request, insurance_number, patientno):

    confirm_form_template = "admin_app/partials/__confirm_patient_assign.html"
    # select membership type
    if request.method == "POST":
        if request.POST.get("assign_family"):

            if ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno):
                messages.add_message(request, messages.ERROR, _("Patient already has an insurance"))
                return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

            insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance_number)
            
            if not insurances:
                messages.add_message(request, messages.ERROR, _("Insurance record not found"))
                return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

            patient = ClinicModels.Patients.objects.using("clinic").filter(patientno=patientno)
            if not patient:
                messages.add_message(request, messages.ERROR, _("Patient record not found"))
                return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

            # save patient to our db
            patient = clone_patient(patient.first())
            if not patient:
                messages.add_message(request, messages.ERROR, _("Incomplete Operation, contact support"))
                return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

            member = ManagerModels.FamilyMember(
                family=insurances.first().family,
                patient=patient,
                status=False
            )
            member.save()


            # notify principle

            if len(ManagerModels.FamilyMember.objects.all()) > 1:
                try:
                    principle_type = ManagerModels.RelationshipType.objects.filter(name__icontains="principle")
                    
                    principles = ManagerModels.FamilyMember.objects.filter(family=member.family, relationship=principle_type.first().id)
                    if not principles:
                        member.delete()
                        messages.add_message(request, messages.ERROR, _("No Principle found for this family"))
                        return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))
                    # get family principle

                    print("\n\n\n")
                    print(principles)
                    print(principles.first().patient.email)
                    print([ p.patient.email for p in principles if p.patient.email ])
                    print("\n\n\n")
                    principle_emails = [ p.patient.email for p in principles if p.patient.email ]
                    if not principle_emails:
                        member.delete()
                        messages.add_message(request, messages.ERROR, _("No Principle email found for this family"))
                        return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

                    # send email to one principle
                    if not principles[0].scheme_no:
                        member.delete()
                        messages.add_message(request, messages.ERROR, _("Principle scheme number not set."))
                        return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

                    combined_string = f"{principles[0].scheme_no}:{member.scheme_no}"

                    domain = get_current_site(request).domain
                    # verification link
                    uidb64 = urlsafe_base64_encode(force_bytes(combined_string))
                    domain = get_current_site(request).domain
                    verify_link = f"http://{domain}" + reverse("activate_family_member", kwargs={"uidb64": uidb64})

                    # verification link
                    uidb64 = urlsafe_base64_encode(force_bytes(combined_string))
                    domain = get_current_site(request).domain
                    decline_link = f"http://{domain}" + reverse("decline_family_member", kwargs={"uidb64": uidb64})

                    subject = 'New Member added to your insurance plan'
                    message = f'A new member is being added to your insurance plan.\n\nUse this link to verify {verify_link}\n\nUse this link to decline {decline_link}'
                    from_email = settings.SUPPORT_EMAIL
                    recipient_list = [principle_emails[0]]

                    send_mail(subject, message, from_email, recipient_list)
                    
                    messages.add_message(request, messages.SUCCESS, _(f"Verification email sent to principle {principles[0].patient.firstname} {principles[0].patient.lastname} via {principles[0].patient.email}"))
                    
                except Exception as err:
                    messages.add_message(request, messages.ERROR, _("Error sending email to principle"))
                    member.delete()


        elif request.POST.get("assign_membership"):
            pass

        elif request.POST.get("suspend"):

            family_member = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
            if not family_member:
                messages.add_message(request, messages.ERROR, _("Record not found."))

            family_member = family_member.first()
            family_member.status = False
            family_member.save()

        elif request.POST.get("activate"):
            family_member = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
            if not family_member:
                messages.add_message(request, messages.ERROR, _("Record not found."))
            
            family_member = family_member.first()
            family_member.status = True
            family_member.save()
    else:
        messages.add_message(request, messages.ERROR, _("Method not allowed."))
    
    return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

class CreditAccountView(AdminAndAuthenticatedAccessMixin, View):
    template_partial_confirm_form = "admin_app/partials/__credit_account.html"
    context_data = {}

    def get(self, request, insurance_number):
        insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance_number)

        if not insurances:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

        insurance = insurances.first()
        self.context_data["insurance"] = insurance
        
        return render(request, template_name=self.template_partial_confirm_form, context=self.context_data)

    def post(self, request, insurance_number):
        if request.POST.get("credit"):
            credit_account = request.POST.get("credit_account")

            insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance_number)
            if not insurances:
                messages.add_message(request, messages.ERROR, _("Insurance record not found."))
                return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))

            insurance = insurances.first()
            insurance.credit = insurance.credit + decimal.Decimal(str(credit_account))
            insurance.save()
            return redirect(reverse("admin_app:insurance-details", args=[insurance_number]))
    
class AdminPatientDetialView(AdminAndAuthenticatedAccessMixin, View):
    template_name = "admin_app/patient_details.html"
    context_data = {}

    def get_patient(self, patientno, commit=True):
        # check if patient exists in our database
        patients = ManagerModels.Patient.objects.filter(patientno=patientno)
        
        if not patients:
            patients = ClinicModels.Patients.objects.using("clinic").filter(patientno=patientno)
            return clone_patient(patients.first(), commit), False

        if not patients:
            # patient not found in clinicMas database
            messages.add_message(self.request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:home"))

        return patients.first(), True

    def get(self, request, patientno):
        patient, is_benefician = self.get_patient(patientno, commit=False)

        if not is_benefician:
            messages.add_message(self.request, messages.ERROR, _("Patient not a benefician of any insurance"))
        else:
            family_member = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno).first()
            self.context_data["family_member"] = family_member
            if family_member:
                insurance = ManagerModels.FamilyInsurance.objects.filter(family=family_member.family).first()
                self.context_data["insurance"] = insurance
            
        self.context_data["patient"] = patient
        self.context_data["form"] = ManagerForms.PatientForm(instance=patient)
        
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request, patientno):
        patient, is_benefician = self.get_patient(patientno, commit=False)

        if not is_benefician:
            messages.add_message(self.request, messages.ERROR, _("Patient not a benefician of any insurance"))
            
        self.context_data["patient"] = patient

        # check is record exists
        instance = ManagerModels.Patient.objects.filter(patientno=request.POST.get("patientno"))
        if instance:
            form = ManagerForms.PatientForm(request.POST, instance=instance.first())
        else:
            form = ManagerForms.PatientForm(request.POST)

            # copy all fields

        if not form.is_valid:
            messages.add_message(request, messages.ERROR, _("Error Processing data."))
        else:
            form.save()
            
        return redirect(reverse("admin_app:patient-details", args=[patientno]))

class AdminPatientInsuranceDetailsView(AdminAndAuthenticatedAccessMixin, View):
    template_partial_confirm_form = "admin_app/partials/__patient_insurance_details.html"
    context_data = {}

    def get_patient(self, patientno, commit=True):
        # check if patient exists in our database
        patients = ManagerModels.Patient.objects.filter(patientno=patientno)
        
        if not patients:
            patients = ClinicModels.Patients.objects.using("clinic").filter(patientno=patientno)
            return clone_patient(patients.first(), commit), False

        if not patients:
            # patient not found in clinicMas database
            messages.add_message(self.request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:home"))

        return patients.first(), True


    def get(self, request, patientno):
        patient, is_benefician = self.get_patient(patientno)

        if not is_benefician:
            messages.add_message(self.request, messages.ERROR, _("Patient not a benefician of any insurance"))
            
        self.context_data["patient"] = patient
        
        # check if patient is in family
        members = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
        if members:
            member = members.first()
        else:
            member = ManagerModels.FamilyMember(
                patient=patient
            )

        form = ManagerForms.FamilyMemberForm(instance=member)
        self.context_data["form"] = form
        
        return render(request, template_name=self.template_partial_confirm_form, context=self.context_data)
    
    
    def post(self, request, patientno):
        patient, is_benefician = self.get_patient(patientno)
        
        # check if patient is in family
        members = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
        if members:
            member = members.first()
            form = ManagerForms.FamilyMemberForm(request.POST, instance=member)
        else:
            # adding new member to family
            form = ManagerForms.FamilyMemberForm(request.POST)
        if form:
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Details updated/saved successfully"))
        else:
            messages.add_message(request, messages.ERROR, _("Incomplete Operation, contact support"))
            
        return redirect(reverse("admin_app:patient-details", args=[patientno]))
        

class PrincipleDocumentView(AdminAndAuthenticatedAccessMixin, View):
    template_partial_confirm_form = "admin_app/partials/__insurance_documents.html"
    context_data = {}
    def get(self, request, patientno):
        members = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
        if not members:
            messages.add_message(request, messages.ERROR, _("Record not found"))

        instance = members.first()
        if instance.relationship != "principle":
            messages.add_message(request, messages.ERROR, _("This action is restricted to principles"))

        self.context_data["instance"] = instance
        return render(request, template_name=self.template_partial_confirm_form, context=self.context_data)

    def post(self, request, patientno):
        moa_doc = request.FILES.get("moa_doc")
        # check if he is a principle
        members = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
        if not members:
            messages.add_message(request, messages.ERROR, _("Record not found"))

        instance = members.first()
        if instance.relationship != "principle":
            messages.add_message(request, messages.ERROR, _("This action is restricted to principles"))

        instance.moa_document = moa_doc
        instance.save()
        messages.add_message(request, messages.SUCCESS, _("MOA document updated"))
        return redirect(reverse("admin_app:patient-details", args=[patientno]))

class AdminPatientMakePaymentsView(AdminAndAuthenticatedAccessMixin, View):
    template_partial_confirm_form = "admin_app/partials/__make_payment.html"
    context_data = {}
    def get(self, request, patientno):
        members = ManagerModels.FamilyMember.objects.filter(patient__patientno=patientno)
        if not members:
            messages.add_message(request, messages.ERROR, _("Patient is not attached to any insurance group"))

        self.context_data["services"] = ManagerModels.Service.objects.all()
        self.context_data["member"] = members.first()
        self.context_data["patient"] = members.first().patient

        return render(request, template_name=self.template_partial_confirm_form, context=self.context_data)
    def post(self, request, patientno):
        return redirect(reverse("admin_app:patient-details", args=[patientno]))


def clone_patient(cm_patient, commit=True):
    patient = ManagerModels.Patient(
        patientid = cm_patient.patientid,
        patientno = cm_patient.patientno,
        nationalidno = cm_patient.nationalidno,
        referenceno = cm_patient.referenceno,
        firstname = cm_patient.firstname,
        lastname = cm_patient.lastname,
        middlename = cm_patient.middlename,
        birthdate = cm_patient.birthdate,
        fingerprint = cm_patient.fingerprint,
        birthplace = cm_patient.birthplace,
        address = cm_patient.address,
        occupation = cm_patient.occupation,
        phone = cm_patient.phone,
        email = cm_patient.email,
        joindate = cm_patient.joindate,
        location = cm_patient.location,
        nokname = cm_patient.nokname,
        nokrelationship = cm_patient.nokrelationship,
        nokphone = cm_patient.nokphone,
        defaultbillno = cm_patient.defaultbillno,
        defaultmembercardno = cm_patient.defaultmembercardno,
        defaultmainmembername = cm_patient.defaultmainmembername,
        enforcedefaultbillno = cm_patient.enforcedefaultbillno,
        hidedetails = cm_patient.hidedetails,
        tinnumber = cm_patient.tinnumber,
    )

    if not patient:
        return None

    if commit:
        patient.save()

    return patient



def VerifyFamilyMemberView(request, uidb64):
    decoded_string = force_str(urlsafe_base64_decode(uidb64))
    principle_sn, member_sn = decoded_string.split(":")

    records = ManagerModels.FamilyMember.objects.filter(scheme_no=member_sn)
    if not records:
        return HttpResponse(status=404)

    family_member = records.first()

    if not family_member.status:
        family_member.status = True
        family_member.save()
        msg = f"Added {family_member.patient.firstname} {family_member.patient.lastname} to {family_member.family.name} insurance"
    else:
        msg = "Expired Link"

    # redirect
    return render(request, template_name="utils/adding_member.html", context={"message":msg})

    
def DeclineFamilyMemberView(request, uidb64):
    decoded_string = force_str(urlsafe_base64_decode(uidb64))
    principle_sn, member_sn = decoded_string.split(":")

    records = ManagerModels.FamilyMember.objects.filter(scheme_no=member_sn)
    if not records:
        return HttpResponse(status=404)

    if not records.first().status:
        msg = f"{records.first().patient.firstname} {records.first().patient.lastname} declined from joining {records.first().family.name} insurance"
        records.first().delete()
    else:
        msg = "Expired Link"    

    # redirect
    return render(request, template_name="utils/adding_member.html", context={"message": msg})


def pdf_view(request, pk):
    instance = ManagerModels.FamilyMember.objects.filter(pk=pk)
    if not instance:
        return HttpResponseNotFound()

    full_path = instance.first().moa_document.path
    
    # Check if the file exists
    if os.path.exists(full_path):
        # Open the file and serve it as a response
        with open(full_path, 'rb') as pdf_file:
            response = FileResponse(pdf_file, content_type='application/pdf')
            return response
    else:
        return HttpResponseNotFound("PDF file not found")