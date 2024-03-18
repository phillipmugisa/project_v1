from django.forms import ModelForm
from manager import models as ManagerModels

class PatientForm(ModelForm):
    class Meta:
        model = ManagerModels.Patient
        fields = ["patientid", "patientno", "nationalidno", "referenceno", 
        "firstname", "lastname", "middlename", "birthdate", 
        "genderid", "birthplace", "address", "occupation", 
        "phone", "email", "location", "nokname", "tinnumber"]

class PatientAddressForm(ModelForm):
    class Meta:
        model = ManagerModels.PatientAddress
        fields = "__all__"
    

class FamilyMemberForm(ModelForm):
    class Meta:
        model = ManagerModels.FamilyMember
        fields = "__all__"