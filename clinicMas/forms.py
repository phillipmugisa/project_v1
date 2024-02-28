from django.forms import ModelForm
from clinicMas import models as ClinicModels

class PatientForm(ModelForm):
    class Meta:
        model = ClinicModels.Patients
        fields = "__all__"