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
from django.shortcuts import get_object_or_404
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


class HomeView(View):
    template_name = "admin_app/index.html"
    template_partial_home = "admin_app/partials/__home.html"

    template_partial_scheme_list = "admin_app/partials/__schemes_list.html"
    context_data = {}

    def get(self, request):
        total_credit = 0
        total_debit = 0
        schemes = ManagerModels.Scheme.objects.filter(status=True)
        translations = ManagerModels.Transaction.objects.all()

        for scheme in schemes:
            total_credit = total_credit + scheme.credit

        for translation in translations:
            total_debit = total_debit + translation.amount_used

        self.context_data["total_credit"] = total_credit
        self.context_data["total_debit"] = total_debit
        self.context_data["schemes"] = schemes
        self.context_data["translations"] = schemes
        self.context_data["beneficiaries"] = ManagerModels.FamilyMember.objects.filter(status=True)

        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        keyword = request.POST.get("search-keyword")
        if not keyword:
            return render(request, template_name=self.template_partial_home, context=self.context_data)

        schemes = ManagerModels.Scheme.objects.filter(Q(name__icontains=keyword) | Q(insurance_number__icontains=keyword))
        self.context_data["schemes"] = schemes
        print("schemes: ", schemes)
        return render(request, template_name=self.template_partial_scheme_list, context=self.context_data)


class SchemeListView(View):
    template_name = "admin_app/schemes.html"
    template_partial_home = "admin_app/partials/__home.html"

    template_partial_scheme_list = "admin_app/partials/__schemes_list.html"
    context_data = {}

    def get(self, request):
        total_credit = 0
        total_debit = 0
        schemes = ManagerModels.Scheme.objects.filter(status=True)
        translations = ManagerModels.Transaction.objects.all()

        for scheme in schemes:
            total_credit = total_credit + scheme.credit

        for translation in translations:
            total_debit = total_debit + translation.amount_used

        self.context_data["total_credit"] = total_credit
        self.context_data["total_debit"] = total_debit
        self.context_data["schemes"] = schemes
        self.context_data["translations"] = schemes
        self.context_data["beneficiaries"] = ManagerModels.FamilyMember.objects.filter(status=True)

        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        keyword = request.POST.get("search-keyword")
        if not keyword:
            return render(request, template_name=self.template_partial_home, context=self.context_data)

        schemes = ManagerModels.Scheme.objects.filter(Q(name__icontains=keyword) | Q(insurance_number__icontains=keyword))
        self.context_data["schemes"] = schemes
        print("schemes: ", schemes)
        return render(request, template_name=self.template_partial_scheme_list, context=self.context_data)

class SchemeDetailsView(View):
    template_name = "admin_app/scheme_details.html"
    template_partial_home = "admin_app/partials/__create_scheme.html"
    context_data = {}

    def get(self, request, insurance_number):
        scheme = get_object_or_404(ManagerModels.Scheme, insurance_number=insurance_number)
        self.context_data["scheme"] = scheme

        
        total_debit = 0
        translations = ManagerModels.Transaction.objects.filter(scheme=scheme)
        self.context_data["translations"] = translations

        for translation in translations:
            total_debit = total_debit + translation.amount_used
        self.context_data["total_debit"] = total_debit

        members = ManagerModels.FamilyMember.objects.filter(scheme=scheme)
        self.context_data["members"] = members

        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request, insurance_number):
        pass

class SchemeCreateView(View):
    template_partial_home = "admin_app/partials/__create_scheme.html"
    context_data = {}

    def get(self, request):
        form = ManagerForms.SchemeForm()
        self.context_data["form"] = form
        total_credit = 0
        total_debit = 0
        schemes = ManagerModels.Scheme.objects.filter(status=True)
        translations = ManagerModels.Transaction.objects.all()

        for scheme in schemes:
            total_credit = total_credit + scheme.credit

        for translation in translations:
            total_debit = total_debit + translation.amount_used

        self.context_data["total_credit"] = total_credit
        self.context_data["total_debit"] = total_debit
        self.context_data["schemes"] = schemes
        self.context_data["translations"] = schemes
        self.context_data["beneficiaries"] = ManagerModels.FamilyMember.objects.filter(status=True)

        return render(request, template_name=self.template_partial_home, context=self.context_data)

    def post(self, request):
        form = ManagerForms.SchemeForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request, messages.SUCCESS, _("Scheme created successfully"))
        else:
            messages.add_message(request, messages.ERROR, _("Unable to create scheme"))
        return redirect("admin_app:schemes")


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