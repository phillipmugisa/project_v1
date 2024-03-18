from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import uuid, os


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}"[:50] + f".{ext}"
    return os.path.join(f"moa/{instance.family.name}/", filename)

class Patient(models.Model):
    patientid = models.IntegerField(db_column='PatientID')
    patientno = models.CharField(db_column='PatientNo', max_length=20, unique=True)
    nationalidno = models.CharField(db_column='NationalIDNo', max_length=20, blank=True, null=True)
    referenceno = models.CharField(db_column='ReferenceNo', max_length=20, blank=True, null=True)
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    genderid = models.CharField(max_length=100, blank=True, null=True)
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)
    fingerprint = models.BinaryField(db_column='Fingerprint', blank=True, null=True)
    birthplace = models.CharField(db_column='BirthPlace', max_length=40, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)
    occupation = models.CharField(db_column='Occupation', max_length=100, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)
    location = models.CharField(db_column='Location', max_length=40, blank=True, null=True)
    nokname = models.CharField(db_column='NOKName', max_length=41, blank=True, null=True)
    nokrelationship = models.CharField(db_column='NOKRelationship', max_length=20, blank=True, null=True)
    nokphone = models.CharField(db_column='NOKPhone', max_length=30, blank=True, null=True)
    defaultbillmodesid = models.CharField(max_length=100, blank=True, null=True)
    defaultbillno = models.CharField(db_column='DefaultBillNo', max_length=20, blank=True, null=True)
    defaultmembercardno = models.CharField(db_column='DefaultMemberCardNo', max_length=30, blank=True, null=True)
    defaultmainmembername = models.CharField(db_column='DefaultMainMemberName', max_length=41, blank=True, null=True)
    enforcedefaultbillno = models.BooleanField(db_column='EnforceDefaultBillNo', blank=True, null=True)
    hidedetails = models.BooleanField(db_column='HideDetails', blank=True, null=True)
    statusid = models.CharField(max_length=100, blank=True, null=True)
    bloodgroupid = models.CharField(max_length=100, blank=True, null=True)
    villagecode = models.CharField(max_length=100, blank=True, null=True)
    tribeid = models.CharField(max_length=100, blank=True, null=True)
    countryid = models.CharField(max_length=100, blank=True, null=True)
    educationlevelid = models.CharField(max_length=100, blank=True, null=True)
    maritalstatusid = models.CharField(max_length=100, blank=True, null=True)
    careentrypointid = models.CharField(max_length=100, blank=True, null=True)
    branchid = models.CharField(max_length=100, blank=True, null=True)
    religionid = models.CharField(max_length=100, blank=True, null=True)
    employer = models.CharField(db_column='Employer', max_length=41, blank=True, null=True)
    employeraddress = models.CharField(db_column='EmployerAddress', max_length=100, blank=True, null=True)
    referringmedicalofficer = models.CharField(db_column='ReferringMedicalOfficer', max_length=41, blank=True, null=True)
    nearestdispensary = models.CharField(db_column='NearestDispensary', max_length=30, blank=True, null=True)
    previousadmissions = models.CharField(db_column='PreviousAdmissions', max_length=30, blank=True, null=True)
    chronicdiseases = models.CharField(db_column='ChronicDiseases', max_length=200, blank=True, null=True)
    firstvisitdate = models.DateTimeField(db_column='FirstVisitDate', blank=True, null=True)
    lastvisitdate = models.DateTimeField(db_column='LastVisitDate', blank=True, null=True)
    combinationon = models.CharField(db_column='CombinationOn', max_length=30, blank=True, null=True)
    totalvisits = models.IntegerField(db_column='TotalVisits', blank=True, null=True)
    accountbalance = models.DecimalField(db_column='AccountBalance', max_digits=19, decimal_places=4, blank=True, null=True)
    xraynumbers = models.DecimalField(db_column='XrayNumbers', max_digits=6, decimal_places=2, blank=True, null=True)
    policenotified = models.BooleanField(db_column='PoliceNotified', blank=True, null=True)
    infectiousdiseasesnotified = models.BooleanField(db_column='InfectiousDiseasesNotified', blank=True, null=True)
    referringfacility = models.CharField(db_column='ReferringFacility', max_length=41, blank=True, null=True)
    medicalconditions = models.CharField(db_column='MedicalConditions', max_length=2000, blank=True, null=True)
    provisionaldiagnosis = models.CharField(db_column='ProvisionalDiagnosis', max_length=2000, blank=True, null=True)
    communityid = models.CharField(max_length=100, blank=True, null=True)
    loginid = models.CharField(max_length=100, blank=True, null=True)
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)
    attachedtoid = models.CharField(max_length=100, blank=True, null=True)
    clientcategoryid = models.CharField(max_length=100, blank=True, null=True)
    healthunitcode = models.CharField(max_length=100, blank=True, null=True)
    accountstatusid = models.CharField(max_length=100, blank=True, null=True)
    opdoutstanding = models.DecimalField(db_column='OPDOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)
    extrabilloutstanding = models.DecimalField(db_column='ExtraBillOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)
    lastaccountactiondate = models.DateTimeField(db_column='LastAccountActionDate', blank=True, null=True)
    knowaboutservice = models.CharField(db_column='KnowAboutService', max_length=100, blank=True, null=True)
    tinnumber = models.CharField(db_column='TINNumber', max_length=20, blank=True, null=True)

    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class PatientAddress(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)

class Family(models.Model):
    name = models.CharField(verbose_name="Family Name", max_length=256, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

class FamilyMember(models.Model):
    # class RelationshipOption(models.TextChoices):
    #     principle = _("principle"), _("principle")
    #     child = _("child"), _("child")
    #     spouse = _("spouse"), _("spouse")

    # default_rel = RelationshipOption.principle       
    # class AccessTypeOption(models.TextChoices):
    #     Premium = _("Premium"), _("Premium")
    #     Gold = _("Gold"), _("Gold")
    #     Silver = _("Silver"), _("Silver")
    #     Basic = _("Basic"), _("Basic")

    # default_access_type = RelationshipOption.principle

    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, null=True, unique=True)
    status = models.BooleanField(default=False)
    relationship = models.ForeignKey(to="RelationshipType", on_delete=models.SET_NULL, null=True)
    access_type = models.ForeignKey(to="InsuranceAccessType", on_delete=models.SET_NULL, null=True)
    scheme_no = models.CharField(_("Scheme Number"), max_length=256, null=True, blank=True)

    moa_document = models.FileField(
        verbose_name=_("MOA Document"),
        upload_to=get_file_path,
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        # if not self.pk and not self.relationship:
        #     self.relationship = self.default_rel
        # if not self.pk and not self.access_type:
        #     self.access_type = self.default_access_type

        # set scheme number
        if not self.scheme_no:
            self.scheme_no = self.generate_scheme_no()
        super().save(*args, **kwargs)

    def generate_scheme_no(self):
        sn = ""
        if self.patient.genderid:
            sn = sn + f"{self.patient.genderid}/"
        if self.patient.nationalidno:
            sn = sn + f"{self.patient.nationalidno}"
            
        sn = sn + f"{self.patient.birthdate.year}/{datetime.now().strftime("%Y-%m-%d")}"
        return sn


    def __str__(self):
        return f"({self.family}) {self.patient.firstname} {self.patient.lastname}"

class InsuranceAccessType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    max_access_amount = models.DecimalField(verbose_name="Maximum Usable Amount", decimal_places=2, max_digits=12, blank=True, null=True)

    def __str__(self):
        return self.name

class RelationshipType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=256)
    max_access_amount = models.DecimalField(verbose_name="Maximum Usable Amount", decimal_places=2, max_digits=12, blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(verbose_name="Family Name", max_length=256)
    price = models.DecimalField(verbose_name="Price of service", decimal_places=2, max_digits=12, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Transaction(models.Model):
    service = models.ForeignKey(to=Service, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(to=Patient, on_delete=models.SET_NULL, null=True)
    amount_user = models.DecimalField(verbose_name="Amount Used", decimal_places=2, max_digits=12, blank=True, null=True)
    completed = models.BooleanField(default=False)
    authorised = models.BooleanField(default=False)

class FamilyInsurance(models.Model):
    insurance_number = models.CharField(db_column='Insurance Number', max_length=100, blank=True, null=True)
    family = models.OneToOneField(to=Family, on_delete=models.SET_NULL, null=True)
    credit = models.DecimalField(verbose_name="Credit On Account", decimal_places=2, max_digits=12, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        if not self.family:
            return self.insurance_number    
        return f"{self.family.name} {self.insurance_number}"

