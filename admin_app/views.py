from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

from manager import models as ManagerModels
from clinicMas import models as ClinicModels
from manager import forms as ManagerForms
from admin_app.mixins import AdminAndAuthenticatedAccessMixin

class AdminHomeView(AdminAndAuthenticatedAccessMixin, View):
    template_name = "admin_app/home.html"
    context_data = {}

    def get(self, request):
        insurances = ManagerModels.FamilyInsurance.objects.all()
        self.context_data["insurances"] = insurances
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        search_keyword = request.POST.get("search_keyword")
        insurances = ManagerModels.FamilyInsurance.objects.filter(Q(insurance_number = search_keyword) | Q(family__name__iexact = search_keyword))

        if not insurances:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return (reverse("admin_app:home"))

        return redirect(reverse("admin_app:insurance-details", args=[insurances.first().insurance_number]))

class AdminInsuranceDetialView(AdminAndAuthenticatedAccessMixin, View):
    template_name = "admin_app/insurance_details.html"
    context_data = {}

    def get(self, request, insurance):
        insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance)

        if not insurances:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:home"))

        self.context_data["insurance"] = insurances.first()
        
        # get family members by family name (lastname)
        family_members = ClinicModels.Patients.objects.using("clinic").filter(lastname__iexact=insurances.first().family.name)

        self.context_data["family_members"] = family_members

        return render(request, template_name=self.template_name, context=self.context_data)
    
class AdminPatientDetialView(AdminAndAuthenticatedAccessMixin, View):
    template_name = "admin_app/patient_details.html"
    context_data = {}

    def get(self, request, insurance, patientid):
        insurances = ManagerModels.FamilyInsurance.objects.filter(insurance_number = insurance)

        if not insurances:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:home"))

        self.context_data["insurance"] = insurances.first()
        
        # get family members by family name (lastname)
        family_members = ClinicModels.Patients.objects.using("clinic").filter(lastname__iexact=insurances.first().family.name)
        self.context_data["family_members"] = family_members

        # filter for specific patient

        # check if patient record was updated
        patients = ManagerModels.Patient.objects.filter(patientid=patientid)
        if not patients:
            patients = family_members.filter(patientid=patientid)

        if not patients:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:insurance-details", args=[insurance]))

        self.context_data["patient"] = patients.first()
        self.context_data["form"] = ManagerForms.PatientForm(instance=patients.first())
        
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request, insurance, patientid):
        insurance = get_object_or_404(ManagerModels.FamilyInsurance, insurance_number = insurance)
        self.context_data["insurance"] = insurance

        family_members = ClinicModels.Patients.objects.using("clinic").filter(lastname__iexact=insurance.family.name)
        self.context_data["family_members"] = family_members

        # filter for specific patient
        patients = family_members.filter(patientid=patientid)
        if not patients:
            messages.add_message(request, messages.ERROR, _("Record not found."))
            return redirect(reverse("admin_app:insurance-details", args=[insurance]))
            
        # process and save data

        # check is record exists
        instance = ManagerModels.Patient.objects.filter(patientid=request.POST.get("patientid"))
        if instance:
            form = ManagerForms.PatientForm(request.POST, instance=instance.first())
        else:
            form = ManagerForms.PatientForm(request.POST)

            # copy all fields

        if not form.is_valid:
            messages.add_message(request, messages.ERROR, _("Error Processing data."))
        else:
            form.save()
            
        return redirect(reverse("admin_app:patient-details", args=[insurance.insurance_number, patientid]))