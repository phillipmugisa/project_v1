# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artregimen(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    combination = models.ForeignKey('Drugcombinations', models.DO_NOTHING, db_column='Combination', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    whostageid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WHOStageID', blank=True, null=True)  # Field name made lowercase.
    druglinesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DrugLinesID', related_name='artregimen_druglinesid_set', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    artcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ARTCategoryID', related_name='artregimen_artcategoryid_set', blank=True, null=True)  # Field name made lowercase.
    whyeligible = models.CharField(db_column='WhyEligible', max_length=200, blank=True, null=True)  # Field name made lowercase.
    artswitchreasons = models.CharField(db_column='ARTSwitchReasons', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    artstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ARTStatusID', related_name='artregimen_artstatusid_set', blank=True, null=True)  # Field name made lowercase.
    refillduration = models.SmallIntegerField(db_column='RefillDuration', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARTRegimen'


class Artregimendetails(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, DrugNo) found, that is not supported. The first column is selected.
    drugno = models.ForeignKey('Drugs', models.DO_NOTHING, db_column='DrugNo')  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARTRegimenDetails'
        unique_together = (('visitno', 'drugno'),)


class Artstopped(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    stopdate = models.DateTimeField(db_column='StopDate', blank=True, null=True)  # Field name made lowercase.
    artstopreasons = models.CharField(db_column='ARTStopReasons', max_length=200, blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARTStopped'


class Accessobjects(models.Model):
    objectname = models.CharField(db_column='ObjectName', primary_key=True, max_length=40)  # Field name made lowercase.
    objectcaption = models.CharField(db_column='ObjectCaption', unique=True, max_length=60)  # Field name made lowercase.
    objecttype = models.CharField(db_column='ObjectType', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccessObjects'


class Accessedcashservices(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ToVisitDate) found, that is not supported. The first column is selected.
    tovisitdate = models.DateTimeField(db_column='ToVisitDate')  # Field name made lowercase.
    authorisedby = models.CharField(db_column='AuthorisedBy', max_length=41, blank=True, null=True)  # Field name made lowercase.
    authorisationreason = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AuthorisationReason', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccessedCashServices'
        unique_together = (('visitno', 'tovisitdate'),)


class Accountactivations(models.Model):
    activationid = models.AutoField(db_column='ActivationID', primary_key=True)  # Field name made lowercase.
    accountbillmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountBillModesID', blank=True, null=True)  # Field name made lowercase.
    accountbillmode = models.CharField(db_column='AccountBillMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountbillno = models.CharField(db_column='AccountBillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    accountstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountStatusID', related_name='accountactivations_accountstatusid_set', blank=True, null=True)  # Field name made lowercase.
    accountstatus = models.CharField(db_column='AccountStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', related_name='accountactivations_entrymodeid_set', blank=True, null=True)  # Field name made lowercase.
    entrymode = models.CharField(db_column='EntryMode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountActivations'


class Accountextrabillpayments(models.Model):
    paytranno = models.OneToOneField('Accounts', models.DO_NOTHING, db_column='PayTranNo', primary_key=True)  # Field name made lowercase. The composite primary key (PayTranNo, ExtraBillNo, TranNo) found, that is not supported. The first column is selected.
    extrabillno = models.ForeignKey('Accountextrabills', models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    tranno = models.ForeignKey('Accountextrabills', models.DO_NOTHING, db_column='TranNo', related_name='accountextrabillpayments_tranno_set')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountExtraBillPayments'
        unique_together = (('paytranno', 'extrabillno', 'tranno'),)


class Accountextrabills(models.Model):
    extrabillno = models.OneToOneField('Extrabills', models.DO_NOTHING, db_column='ExtraBillNo', primary_key=True)  # Field name made lowercase. The composite primary key (ExtraBillNo, TranNo) found, that is not supported. The first column is selected.
    tranno = models.ForeignKey('Accounts', models.DO_NOTHING, db_column='TranNo')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountExtraBills'
        unique_together = (('extrabillno', 'tranno'),)


class Accountinvoicepayments(models.Model):
    paytranno = models.OneToOneField('Accounts', models.DO_NOTHING, db_column='PayTranNo', primary_key=True)  # Field name made lowercase. The composite primary key (PayTranNo, InvoiceNo, TranNo) found, that is not supported. The first column is selected.
    invoiceno = models.ForeignKey('Accountinvoices', models.DO_NOTHING, db_column='InvoiceNo')  # Field name made lowercase.
    tranno = models.ForeignKey('Accountinvoices', models.DO_NOTHING, db_column='TranNo', related_name='accountinvoicepayments_tranno_set')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountInvoicePayments'
        unique_together = (('paytranno', 'invoiceno', 'tranno'),)


class Accountinvoices(models.Model):
    invoiceno = models.OneToOneField('Invoices', models.DO_NOTHING, db_column='InvoiceNo', primary_key=True)  # Field name made lowercase. The composite primary key (InvoiceNo, TranNo) found, that is not supported. The first column is selected.
    tranno = models.ForeignKey('Accounts', models.DO_NOTHING, db_column='TranNo')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountInvoices'
        unique_together = (('invoiceno', 'tranno'),)


class Accountstatement(models.Model):
    transactionid = models.AutoField(db_column='TransactionID', primary_key=True)  # Field name made lowercase.
    transactionalno = models.CharField(db_column='TransactionalNo', max_length=20)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    billmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BillModesID', blank=True, null=True)  # Field name made lowercase.
    tobillcustomerno = models.CharField(db_column='ToBillCustomerNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insuranceno = models.CharField(db_column='InsuranceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(db_column='MemberCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    accountactionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountActionID', related_name='accountstatement_accountactionid_set', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountStatement'
        unique_together = (('transactionalno', 'objectname'),)


class Accounttransferdetails(models.Model):
    tranno = models.OneToOneField('Accounts', models.DO_NOTHING, db_column='TranNo', primary_key=True)  # Field name made lowercase.
    fromaccount = models.CharField(db_column='FromAccount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    toaccount = models.ForeignKey('Billcustomers', models.DO_NOTHING, db_column='ToAccount', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountinwords = models.CharField(db_column='AmountInWords', max_length=500, blank=True, null=True)  # Field name made lowercase.
    reason = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransferDetails'


class Accountwithdrawapprovals(models.Model):
    requestno = models.OneToOneField('Accountwithdrawrequests', models.DO_NOTHING, db_column='RequestNo', primary_key=True)  # Field name made lowercase.
    accountbillmodes = models.CharField(db_column='AccountBillModes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    approvaldate = models.DateTimeField(db_column='ApprovalDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    requeststatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RequestStatusID', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountWithdrawApprovals'


class Accountwithdrawrequests(models.Model):
    requestid = models.IntegerField(db_column='RequestID')  # Field name made lowercase.
    requestno = models.CharField(db_column='RequestNo', primary_key=True, max_length=20)  # Field name made lowercase.
    accountbillmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountBillModesID', blank=True, null=True)  # Field name made lowercase.
    accountbillmodes = models.CharField(db_column='AccountBillModes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountbillno = models.CharField(db_column='AccountBillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    withdrawtypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WithdrawTypeID', related_name='accountwithdrawrequests_withdrawtypeid_set', blank=True, null=True)  # Field name made lowercase.
    withdrawtype = models.CharField(db_column='WithdrawType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    requestdate = models.DateTimeField(db_column='RequestDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    withdrawrequestreasonid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WithdrawRequestReasonID', related_name='accountwithdrawrequests_withdrawrequestreasonid_set', blank=True, null=True)  # Field name made lowercase.
    withdrawrequestreason = models.CharField(db_column='WithdrawRequestReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastvaliditydatetime = models.DateTimeField(db_column='LastValidityDateTime', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    requeststatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RequestStatusID', related_name='accountwithdrawrequests_requeststatusid_set', blank=True, null=True)  # Field name made lowercase.
    requeststatus = models.CharField(db_column='RequestStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountWithdrawRequests'


class Accounts(models.Model):
    accountid = models.AutoField(primary_key=True, db_column='AccountID')  # Field name made lowercase.
    tranid = models.IntegerField(db_column='TranID')  # Field name made lowercase.
    tranno = models.CharField(db_column='TranNo', max_length=20)  # Field name made lowercase.
    clientfullname = models.CharField(db_column='ClientFullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accountbillmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountBillModesID', blank=True, null=True)  # Field name made lowercase.
    accountbillno = models.CharField(db_column='AccountBillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
    paymodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayModesID', related_name='accounts_paymodesid_set', blank=True, null=True)  # Field name made lowercase.
    accountactionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountActionID', related_name='accounts_accountactionid_set', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrenciesID', related_name='accounts_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    amounttendered = models.DecimalField(db_column='AmountTendered', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    accountgroupid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountGroupID', related_name='accounts_accountgroupid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', related_name='accounts_entrymodeid_set', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BranchID', related_name='accounts_branchid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    receiptbalance = models.DecimalField(db_column='ReceiptBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    requestno = models.ForeignKey(Accountwithdrawapprovals, models.DO_NOTHING, db_column='RequestNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Accounts'


class Accountsext(models.Model):
    tranno = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='TranNo', primary_key=True)  # Field name made lowercase. The composite primary key (TranNo, ReferenceNo) found, that is not supported. The first column is selected.
    referenceno = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='ReferenceNo', related_name='accountsext_referenceno_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountsEXT'
        unique_together = (('tranno', 'referenceno'),)


class Activeusers(models.Model):
    loginid = models.OneToOneField('Logins', models.DO_NOTHING, db_column='LoginID', primary_key=True)  # Field name made lowercase. The composite primary key (LoginID, ClientMachine) found, that is not supported. The first column is selected.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    logindate = models.DateTimeField(db_column='LoginDate', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    nologins = models.SmallIntegerField(db_column='NoLogins', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActiveUsers'
        unique_together = (('loginid', 'clientmachine'),)


class Admissions(models.Model):
    admissionid = models.IntegerField(db_column='AdmissionID')  # Field name made lowercase.
    admissionno = models.CharField(db_column='AdmissionNo', primary_key=True, max_length=20)  # Field name made lowercase.
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    bedno = models.ForeignKey('Beds', models.DO_NOTHING, db_column='BedNo', blank=True, null=True)  # Field name made lowercase.
    patientno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    chartnumber = models.CharField(db_column='ChartNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    admissiondatetime = models.DateTimeField(db_column='AdmissionDateTime', blank=True, null=True)  # Field name made lowercase.
    billmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BillModesID', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insuranceno = models.CharField(db_column='InsuranceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    associatedbillno = models.ForeignKey('Billcustomers', models.DO_NOTHING, db_column='AssociatedBillNo', blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(db_column='MemberCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mainmembername = models.CharField(db_column='MainMemberName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    claimreferenceno = models.CharField(db_column='ClaimReferenceNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    copaytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoPayTypeID', related_name='admissions_copaytypeid_set', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    copayvalue = models.DecimalField(db_column='CoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    accesscashservices = models.BooleanField(db_column='AccessCashServices', blank=True, null=True)  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(db_column='SmartCardApplicable', blank=True, null=True)  # Field name made lowercase.
    admissionnotes = models.CharField(db_column='AdmissionNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    admissionstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AdmissionStatusID', related_name='admissions_admissionstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    servicecode = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceCode', blank=True, null=True)  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(db_column='ProvisionalDiagnosis', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Admissions'


class Alerts(models.Model):
    alertid = models.AutoField(db_column='AlertID', primary_key=True)  # Field name made lowercase.
    alerttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AlertTypeID', blank=True, null=True)  # Field name made lowercase.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    sentdate = models.DateTimeField(db_column='SentDate', blank=True, null=True)  # Field name made lowercase.
    senttime = models.CharField(db_column='SentTime', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alerts'
        unique_together = (('alerttypeid', 'visitno', 'sentdate'),)


class Allergies(models.Model):
    allergyno = models.CharField(db_column='AllergyNo', primary_key=True, max_length=20)  # Field name made lowercase.
    allergyname = models.CharField(db_column='AllergyName', unique=True, max_length=60, blank=True, null=True)  # Field name made lowercase.
    allergycategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AllergyCategoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Allergies'


class Allergydrugs(models.Model):
    allergyno = models.OneToOneField(Allergies, models.DO_NOTHING, db_column='AllergyNo', primary_key=True)  # Field name made lowercase. The composite primary key (AllergyNo, DrugNo) found, that is not supported. The first column is selected.
    drugno = models.ForeignKey('Drugs', models.DO_NOTHING, db_column='DrugNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllergyDrugs'
        unique_together = (('allergyno', 'drugno'),)


class Alternatedrugs(models.Model):
    drugno = models.OneToOneField('Drugs', models.DO_NOTHING, db_column='DrugNo', primary_key=True)  # Field name made lowercase. The composite primary key (DrugNo, AlternateDrugNo) found, that is not supported. The first column is selected.
    alternatedrugno = models.ForeignKey('Drugs', models.DO_NOTHING, db_column='AlternateDrugNo', related_name='alternatedrugs_alternatedrugno_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlternateDrugs'
        unique_together = (('drugno', 'alternatedrugno'),)


class Antenatal(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    infection = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='Infection', blank=True, null=True)  # Field name made lowercase.
    infectiondetails = models.CharField(db_column='InfectionDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    accidentduringpregnancy = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccidentDuringPregnancy', related_name='antenatal_accidentduringpregnancy_set', blank=True, null=True)  # Field name made lowercase.
    detailsofaccident = models.CharField(db_column='DetailsOfAccident', max_length=100, blank=True, null=True)  # Field name made lowercase.
    useofdrugsorprescription = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='UseOfDrugsOrPrescription', related_name='antenatal_useofdrugsorprescription_set', blank=True, null=True)  # Field name made lowercase.
    drugdetails = models.CharField(db_column='DrugDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    smoking = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='Smoking', related_name='antenatal_smoking_set', blank=True, null=True)  # Field name made lowercase.
    chronicillness = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ChronicIllness', related_name='antenatal_chronicillness_set', blank=True, null=True)  # Field name made lowercase.
    detailsofillness = models.CharField(db_column='DetailsOfIllness', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Antenatal'


class Antenatalenrollment(models.Model):
    ancid = models.IntegerField(db_column='ANCID', blank=True, null=True)  # Field name made lowercase.
    ancno = models.CharField(db_column='ANCNo', primary_key=True, max_length=20)  # Field name made lowercase.
    patientno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    hivstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVStatusID', blank=True, null=True)  # Field name made lowercase.
    partnershivstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PartnersHIVStatusID', related_name='antenatalenrollment_partnershivstatusid_set', blank=True, null=True)  # Field name made lowercase.
    gravida = models.IntegerField(db_column='Gravida', blank=True, null=True)  # Field name made lowercase.
    para = models.CharField(db_column='Para', max_length=41, blank=True, null=True)  # Field name made lowercase.
    lnmp = models.DateTimeField(db_column='LNMP', blank=True, null=True)  # Field name made lowercase.
    lnmpdatereliable = models.BooleanField(db_column='LNMPDateReliable', blank=True, null=True)  # Field name made lowercase.
    cycleregularid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CycleRegularID', related_name='antenatalenrollment_cycleregularid_set', blank=True, null=True)  # Field name made lowercase.
    edd = models.DateTimeField(db_column='EDD', blank=True, null=True)  # Field name made lowercase.
    scandate = models.DateTimeField(db_column='ScanDate', blank=True, null=True)  # Field name made lowercase.
    medicalhistory = models.CharField(db_column='MedicalHistory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    medicalhistorynotes = models.CharField(db_column='MedicalHistoryNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    bloodtransfusion = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BloodTransfusion', related_name='antenatalenrollment_bloodtransfusion_set', blank=True, null=True)  # Field name made lowercase.
    bloodtransfusiondate = models.DateTimeField(db_column='BloodTransfusionDate', blank=True, null=True)  # Field name made lowercase.
    surgicalhistory = models.CharField(db_column='SurgicalHistory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    surgicalhistorynotes = models.CharField(db_column='SurgicalHistoryNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    gynaecologicalhistory = models.CharField(db_column='GynaecologicalHistory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gynaecologicalhistorynotes = models.CharField(db_column='GynaecologicalHistoryNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    familyhistory = models.CharField(db_column='FamilyHistory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    familyhistorynotes = models.CharField(db_column='FamilyHistoryNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    socialhistory = models.CharField(db_column='SocialHistory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    socialhistorynotes = models.CharField(db_column='SocialHistoryNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    patientstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PatientStatusID', related_name='antenatalenrollment_patientstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    donepregnancyscanid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DonePregnancyScanID', related_name='antenatalenrollment_donepregnancyscanid_set', blank=True, null=True)  # Field name made lowercase.
    enrollmentdate = models.DateTimeField(db_column='EnrollmentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AntenatalEnrollment'


class Antenatalvisits(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    ancno = models.ForeignKey(Antenatalenrollment, models.DO_NOTHING, db_column='ANCNo', blank=True, null=True)  # Field name made lowercase.
    pallorid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PallorID', blank=True, null=True)  # Field name made lowercase.
    jaundiceid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='JaundiceID', related_name='antenatalvisits_jaundiceid_set', blank=True, null=True)  # Field name made lowercase.
    lynphadenopathyid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LynphadenopathyID', related_name='antenatalvisits_lynphadenopathyid_set', blank=True, null=True)  # Field name made lowercase.
    varicoseid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VaricoseID', related_name='antenatalvisits_varicoseid_set', blank=True, null=True)  # Field name made lowercase.
    oedemaid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='OedemaID', related_name='antenatalvisits_oedemaid_set', blank=True, null=True)  # Field name made lowercase.
    heartsoundid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HeartSoundID', related_name='antenatalvisits_heartsoundid_set', blank=True, null=True)  # Field name made lowercase.
    airentryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AirEntryID', related_name='antenatalvisits_airentryid_set', blank=True, null=True)  # Field name made lowercase.
    breastid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BreastID', related_name='antenatalvisits_breastid_set', blank=True, null=True)  # Field name made lowercase.
    liverid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LiverID', related_name='antenatalvisits_liverid_set', blank=True, null=True)  # Field name made lowercase.
    spleenid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SpleenID', related_name='antenatalvisits_spleenid_set', blank=True, null=True)  # Field name made lowercase.
    bowelsoundsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BowelSoundsID', related_name='antenatalvisits_bowelsoundsid_set', blank=True, null=True)  # Field name made lowercase.
    scarid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ScarID', related_name='antenatalvisits_scarid_set', blank=True, null=True)  # Field name made lowercase.
    pupilreactionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PupilReactionID', related_name='antenatalvisits_pupilreactionid_set', blank=True, null=True)  # Field name made lowercase.
    reflexesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReflexesID', related_name='antenatalvisits_reflexesid_set', blank=True, null=True)  # Field name made lowercase.
    otherstiid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='OtherSTIID', related_name='antenatalvisits_otherstiid_set', blank=True, null=True)  # Field name made lowercase.
    stidetails = models.CharField(db_column='STIDetails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    skeletaldeformityid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SkeletalDeformityID', related_name='antenatalvisits_skeletaldeformityid_set', blank=True, null=True)  # Field name made lowercase.
    anenorrheaweeks = models.IntegerField(db_column='AnenorrheaWeeks', blank=True, null=True)  # Field name made lowercase.
    fundalheight = models.CharField(db_column='FundalHeight', max_length=10, blank=True, null=True)  # Field name made lowercase.
    presentationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PresentationID', related_name='antenatalvisits_presentationid_set', blank=True, null=True)  # Field name made lowercase.
    lieid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LieID', related_name='antenatalvisits_lieid_set', blank=True, null=True)  # Field name made lowercase.
    positionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PositionID', related_name='antenatalvisits_positionid_set', blank=True, null=True)  # Field name made lowercase.
    relationpporbrim = models.CharField(db_column='RelationPPOrBrim', max_length=10, blank=True, null=True)  # Field name made lowercase.
    foetalheart = models.IntegerField(db_column='FoetalHeart', blank=True, null=True)  # Field name made lowercase.
    ttgiven = models.BooleanField(db_column='TTGiven', blank=True, null=True)  # Field name made lowercase.
    iptid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='IPTID', related_name='antenatalvisits_iptid_set', blank=True, null=True)  # Field name made lowercase.
    netuseid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='NetUseID', related_name='antenatalvisits_netuseid_set', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    returndate = models.DateTimeField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    doctorspecialityid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DoctorSpecialityID', related_name='antenatalvisits_doctorspecialityid_set', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey('Staff', models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    nurseinchargeid = models.ForeignKey('Staff', models.DO_NOTHING, db_column='NurseInChargeID', related_name='antenatalvisits_nurseinchargeid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AntenatalVisits'


class Appointments(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, StartDate) found, that is not supported. The first column is selected.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    appointmentprecisionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AppointmentPrecisionID', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    duration = models.SmallIntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DoctorSpecialtyID', related_name='appointments_doctorspecialtyid_set', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    appointmentcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AppointmentCategoryID', related_name='appointments_appointmentcategoryid_set', blank=True, null=True)  # Field name made lowercase.
    communityid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CommunityID', related_name='appointments_communityid_set', blank=True, null=True)  # Field name made lowercase.
    appointmentdes = models.CharField(db_column='AppointmentDes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appointmentstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AppointmentStatusID', related_name='appointments_appointmentstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appointments'
        unique_together = (('patientno', 'startdate'),)


class Assetmaintainancelog(models.Model):
    serialno = models.OneToOneField('Assetregister', models.DO_NOTHING, db_column='SerialNo', primary_key=True)  # Field name made lowercase. The composite primary key (SerialNo, MaintainanceDate) found, that is not supported. The first column is selected.
    actiontaken = models.CharField(db_column='ActionTaken', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maintainancedate = models.DateTimeField(db_column='MaintainanceDate')  # Field name made lowercase.
    maintainedby = models.CharField(db_column='MaintainedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maintainacecost = models.DecimalField(db_column='MaintainaceCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nextdue = models.DateTimeField(db_column='NextDue', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssetMaintainanceLog'
        unique_together = (('serialno', 'maintainancedate'),)


class Assetregister(models.Model):
    serialno = models.CharField(db_column='SerialNo', primary_key=True, max_length=20)  # Field name made lowercase.
    manufacturerid = models.CharField(db_column='ManufacturerID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    institutionalid = models.CharField(db_column='InstitutionalID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    assetsourceid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AssetSourceID', blank=True, null=True)  # Field name made lowercase.
    assetcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AssetCategoryID', related_name='assetregister_assetcategoryid_set', blank=True, null=True)  # Field name made lowercase.
    deptid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DeptID', related_name='assetregister_deptid_set', blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.CharField(db_column='ItemDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=200, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    dateofpurchase = models.DateTimeField(db_column='DateOfPurchase', blank=True, null=True)  # Field name made lowercase.
    supplierno = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierNo', blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    dateofdelivery = models.DateTimeField(db_column='DateOfDelivery', blank=True, null=True)  # Field name made lowercase.
    salvagevalue = models.IntegerField(db_column='SalvageValue', blank=True, null=True)  # Field name made lowercase.
    depreciationrate = models.IntegerField(db_column='DepreciationRate', blank=True, null=True)  # Field name made lowercase.
    usefullife = models.IntegerField(db_column='UsefulLife', blank=True, null=True)  # Field name made lowercase.
    depreciationmethodid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DepreciationMethodID', related_name='assetregister_depreciationmethodid_set', blank=True, null=True)  # Field name made lowercase.
    depreciationstartdate = models.DateTimeField(db_column='DepreciationStartDate', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.CharField(db_column='AssignedTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicingschedule = models.IntegerField(db_column='ServicingSchedule', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssetRegister'


class Associatedbillcustomers(models.Model):
    accountno = models.OneToOneField('Billcustomers', models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, AssociatedBillNo) found, that is not supported. The first column is selected.
    associatedbillno = models.ForeignKey('Billcustomers', models.DO_NOTHING, db_column='AssociatedBillNo', related_name='associatedbillcustomers_associatedbillno_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssociatedBillCustomers'
        unique_together = (('accountno', 'associatedbillno'),)


class Attachpackage(models.Model):
    attachpackageid = models.AutoField(primary_key=True, db_column='AttachPackageID')  # Field name made lowercase.
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase. The composite primary key (VisitNo, PackageNo) found, that is not supported. The first column is selected.
    patientno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    packageno = models.ForeignKey('Packages', models.DO_NOTHING, db_column='PackageNo')  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=200, blank=True, null=True)  # Field name made lowercase.
    packagevisitno = models.CharField(db_column='PackageVisitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    packagestartdate = models.DateTimeField(db_column='PackageStartDate', blank=True, null=True)  # Field name made lowercase.
    packageenddate = models.DateTimeField(db_column='PackageEndDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttachPackage'
        unique_together = (('visitno', 'packageno'),)


class Audittrail(models.Model):
    auditid = models.AutoField(db_column='AuditID', primary_key=True)  # Field name made lowercase.
    auditaction = models.CharField(db_column='AuditAction', max_length=1)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=40)  # Field name made lowercase.
    fulldate = models.DateTimeField(db_column='FullDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuditTrail'


class Audittraildetails(models.Model):
    auditid = models.OneToOneField(Audittrail, models.DO_NOTHING, db_column='AuditID', primary_key=True)  # Field name made lowercase. The composite primary key (AuditID, ColumnName) found, that is not supported. The first column is selected.
    columnname = models.CharField(db_column='ColumnName', max_length=60)  # Field name made lowercase.
    originalvalue = models.CharField(db_column='OriginalValue', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    newvalue = models.CharField(db_column='NewValue', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuditTrailDetails'
        unique_together = (('auditid', 'columnname'),)


class Autonumbers(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName', primary_key=True)  # Field name made lowercase. The composite primary key (ObjectName, AutoColumnName) found, that is not supported. The first column is selected.
    autocolumnname = models.CharField(db_column='AutoColumnName', max_length=60)  # Field name made lowercase.
    helpercolumnname = models.CharField(db_column='HelperColumnName', max_length=60)  # Field name made lowercase.
    autocolumnlen = models.SmallIntegerField(db_column='AutoColumnLEN')  # Field name made lowercase.
    paddingchar = models.CharField(db_column='PaddingCHAR', max_length=1)  # Field name made lowercase.
    paddinglen = models.SmallIntegerField(db_column='PaddingLEN')  # Field name made lowercase.
    separatorchar = models.CharField(db_column='SeparatorCHAR', max_length=1)  # Field name made lowercase.
    separatorpositions = models.CharField(db_column='SeparatorPositions', max_length=20, blank=True, null=True)  # Field name made lowercase.
    startvalue = models.IntegerField(db_column='StartValue')  # Field name made lowercase.
    increment = models.SmallIntegerField(db_column='Increment')  # Field name made lowercase.
    allowjumpto = models.BooleanField(db_column='AllowJumpTo')  # Field name made lowercase.
    jumptovalue = models.IntegerField(db_column='JumpToValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutoNumbers'
        unique_together = (('objectname', 'autocolumnname'),)


class Bankaccounts(models.Model):
    accountno = models.CharField(db_column='AccountNo', primary_key=True, max_length=20)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    banknameid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BankNameID', blank=True, null=True)  # Field name made lowercase.
    currencyid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrencyID', related_name='bankaccounts_currencyid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankAccounts'


class Bankpaymentdetails(models.Model):
    receiptno = models.CharField(db_column='ReceiptNo', primary_key=True, max_length=10)  # Field name made lowercase.
    banknamesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BankNamesID', blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paymodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayModesID', related_name='bankpaymentdetails_paymodesid_set', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankPaymentDetails'


class Bankingregister(models.Model):
    registerid = models.IntegerField(db_column='RegisterID')  # Field name made lowercase.
    registerno = models.CharField(db_column='RegisterNo', primary_key=True, max_length=20)  # Field name made lowercase.
    collectionstartdate = models.DateTimeField(db_column='CollectionStartDate', blank=True, null=True)  # Field name made lowercase.
    collectionenddate = models.DateTimeField(db_column='CollectionEndDate', blank=True, null=True)  # Field name made lowercase.
    bankingdate = models.DateTimeField(db_column='BankingDate', blank=True, null=True)  # Field name made lowercase.
    banknameid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BankNameID', blank=True, null=True)  # Field name made lowercase.
    collectionsourcetypeid = models.CharField(db_column='CollectionSourceTypeID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    accountno = models.ForeignKey(Bankaccounts, models.DO_NOTHING, db_column='AccountNo', blank=True, null=True)  # Field name made lowercase.
    amountcollected = models.DecimalField(db_column='AmountCollected', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountbanked = models.DecimalField(db_column='AmountBanked', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountinwords = models.CharField(db_column='AmountInWords', max_length=800, blank=True, null=True)  # Field name made lowercase.
    currencyid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrencyID', related_name='bankingregister_currencyid_set', blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bankedby = models.CharField(db_column='BankedBy', max_length=40, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankingRegister'


class Bankingregisterdetails(models.Model):
    registerno = models.OneToOneField(Bankingregister, models.DO_NOTHING, db_column='RegisterNo', primary_key=True)  # Field name made lowercase. The composite primary key (RegisterNo, CollectionModesID, DocumentNo) found, that is not supported. The first column is selected.
    collectionmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CollectionModesID')  # Field name made lowercase.
    bankmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BankModesID', related_name='bankingregisterdetails_bankmodesid_set', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BankingRegisterDetails'
        unique_together = (('registerno', 'collectionmodesid', 'documentno'),)


class Barcodedetails(models.Model):
    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (ItemCode, ItemCategoryID, RecordDateTime) found, that is not supported. The first column is selected.
    itemcategoryid = models.CharField(db_column='ItemCategoryID', max_length=10)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BarCodeDetails'
        unique_together = (('itemcode', 'itemcategoryid', 'recorddatetime'),)


class Beds(models.Model):
    bedid = models.IntegerField(db_column='BedID')  # Field name made lowercase.
    bedno = models.CharField(db_column='BedNo', primary_key=True, max_length=20)  # Field name made lowercase.
    bedname = models.CharField(db_column='BedName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    roomno = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='RoomNo', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Beds'
        unique_together = (('bedname', 'roomno'),)


class Billadjustments(models.Model):
    adjustmentid = models.IntegerField(db_column='AdjustmentID')  # Field name made lowercase.
    adjustmentno = models.CharField(db_column='AdjustmentNo', primary_key=True, max_length=20)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    adjustmentdate = models.DateTimeField(db_column='AdjustmentDate', blank=True, null=True)  # Field name made lowercase.
    adjustmenttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AdjustmentTypeID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillAdjustments'


class Billcustomfee(models.Model):
    accountno = models.OneToOneField('Billcustomers', models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    customfee = models.DecimalField(db_column='CustomFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrenciesID', related_name='billcustomfee_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    requirespayment = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RequiresPayment', related_name='billcustomfee_requirespayment_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillCustomFee'
        unique_together = (('accountno', 'itemcode', 'itemcategoryid'),)


class Billcustomeritemcategorycopay(models.Model):
    accountno = models.OneToOneField('Billcustomers', models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillCustomerItemCategoryCopay'
        unique_together = (('accountno', 'itemcategoryid'),)


class Billcustomeritemscopay(models.Model):
    accountno = models.OneToOneField('Billcustomers', models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillCustomerItemsCopay'
        unique_together = (('accountno', 'itemcode', 'itemcategoryid'),)


class Billcustomermembers(models.Model):
    medicalcardno = models.CharField(db_column='MedicalCardNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (MedicalCardNo, AccountNo) found, that is not supported. The first column is selected.
    accountno = models.ForeignKey('Billcustomers', models.DO_NOTHING, db_column='AccountNo')  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    policystartdate = models.DateTimeField(db_column='PolicyStartDate', blank=True, null=True)  # Field name made lowercase.
    policyenddate = models.DateTimeField(db_column='PolicyEndDate', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    memberstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='MemberStatusID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillCustomerMembers'
        unique_together = (('medicalcardno', 'accountno'),)


class Billcustomervisittypecopay(models.Model):
    accountno = models.OneToOneField('Billcustomers', models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, VisitTypeID) found, that is not supported. The first column is selected.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID')  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=20)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillCustomerVisitTypeCopay'
        unique_together = (('accountno', 'visittypeid'),)


class Billcustomers(models.Model):
    accountid = models.IntegerField(db_column='AccountID')  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', primary_key=True, max_length=20)  # Field name made lowercase.
    billcustomername = models.CharField(db_column='BillCustomerName', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    billcustomertypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BillCustomerTypeID', blank=True, null=True)  # Field name made lowercase.
    insuranceno = models.ForeignKey('self', models.DO_NOTHING, db_column='InsuranceNo', blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logophoto = models.BinaryField(db_column='LogoPhoto', blank=True, null=True)  # Field name made lowercase.
    memberdeclaration = models.CharField(db_column='MemberDeclaration', max_length=800, blank=True, null=True)  # Field name made lowercase.
    doctordeclaration = models.CharField(db_column='DoctorDeclaration', max_length=800, blank=True, null=True)  # Field name made lowercase.
    copaytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoPayTypeID', related_name='billcustomers_copaytypeid_set', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    copayvalue = models.DecimalField(db_column='CoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    allowonlylistedmember = models.BooleanField(db_column='AllowOnlyListedMember', blank=True, null=True)  # Field name made lowercase.
    usecustomfee = models.BooleanField(db_column='UseCustomFee', blank=True, null=True)  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(db_column='SmartCardApplicable', blank=True, null=True)  # Field name made lowercase.
    capturemembercardno = models.BooleanField(db_column='CaptureMemberCardNo', blank=True, null=True)  # Field name made lowercase.
    captureclaimreferenceno = models.BooleanField(db_column='CaptureClaimReferenceNo', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    accountstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountStatusID', related_name='billcustomers_accountstatusid_set', blank=True, null=True)  # Field name made lowercase.
    accountbalance = models.DecimalField(db_column='AccountBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    opdoutstanding = models.DecimalField(db_column='OPDOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    extrabilloutstanding = models.DecimalField(db_column='ExtraBillOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastaccountactiondate = models.DateTimeField(db_column='LastAccountActionDate', blank=True, null=True)  # Field name made lowercase.
    tinnumber = models.CharField(db_column='TINNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    opdcopayvalue = models.DecimalField(db_column='OPDCoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipdcopayvalue = models.DecimalField(db_column='IPDCoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillCustomers'


class Billexcludeditems(models.Model):
    accountno = models.OneToOneField(Billcustomers, models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillExcludedItems'
        unique_together = (('accountno', 'itemcode', 'itemcategoryid'),)


class Billvisittypecustomfee(models.Model):
    accountno = models.OneToOneField(Billcustomers, models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, ItemCode, ItemCategoryID, VisitTypeID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', related_name='billvisittypecustomfee_visittypeid_set')  # Field name made lowercase.
    customfee = models.DecimalField(db_column='CustomFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrenciesID', related_name='billvisittypecustomfee_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillVisitTypeCustomFee'
        unique_together = (('accountno', 'itemcode', 'itemcategoryid', 'visittypeid'),)


class Billablemappings(models.Model):
    itemcategoryid = models.OneToOneField('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID', primary_key=True)  # Field name made lowercase. The composite primary key (ItemCategoryID, ItemCode, MappedTypeID, AgentNo) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    mappedtypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='MappedTypeID', related_name='billablemappings_mappedtypeid_set')  # Field name made lowercase.
    agentno = models.ForeignKey('Intagents', models.DO_NOTHING, db_column='AgentNo')  # Field name made lowercase.
    mappedcode = models.CharField(db_column='MappedCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=10, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BillableMappings'
        unique_together = (('itemcategoryid', 'itemcode', 'mappedtypeid', 'agentno'),)


class Bulkmessaging(models.Model):
    messageid = models.IntegerField(db_column='MessageID', blank=True, null=True)  # Field name made lowercase.
    messageno = models.CharField(db_column='MessageNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (MessageNo, Message, RecordDateTime) found, that is not supported. The first column is selected.
    phone = models.CharField(db_column='Phone', max_length=7500, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=600)  # Field name made lowercase.
    sentid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SentID', blank=True, null=True)  # Field name made lowercase.
    flagid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='flagID', related_name='bulkmessaging_flagid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    textlifespan = models.IntegerField(db_column='TextLifeSpan', blank=True, null=True)  # Field name made lowercase.
    senddatetime = models.DateTimeField(db_column='SendDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BulkMessaging'
        unique_together = (('messageno', 'message', 'recorddatetime'),)


class Cancerdiagnosis(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, DiseaseNo) found, that is not supported. The first column is selected.
    diseaseno = models.ForeignKey('Cancerdiseases', models.DO_NOTHING, db_column='DiseaseNo')  # Field name made lowercase.
    topographicalno = models.ForeignKey('Topologysites', models.DO_NOTHING, db_column='TopographicalNo', blank=True, null=True)  # Field name made lowercase.
    basisofdiagnosisid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BasisOfDiagnosisID', blank=True, null=True)  # Field name made lowercase.
    cancerstageid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CancerStageID', related_name='cancerdiagnosis_cancerstageid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CancerDiagnosis'
        unique_together = (('visitno', 'diseaseno'),)


class Cancerdiseases(models.Model):
    diseaseid = models.IntegerField(db_column='DiseaseID')  # Field name made lowercase.
    diseaseno = models.CharField(db_column='DiseaseNo', primary_key=True, max_length=20)  # Field name made lowercase.
    diseasecode = models.CharField(db_column='DiseaseCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diseasename = models.CharField(db_column='DiseaseName', max_length=800, blank=True, null=True)  # Field name made lowercase.
    cancerdiseasecategoriesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CancerDiseaseCategoriesID', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CancerDiseases'


class Cardiologyexaminations(models.Model):
    examid = models.IntegerField(db_column='ExamId')  # Field name made lowercase.
    examcode = models.CharField(db_column='ExamCode', primary_key=True, max_length=20)  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    cardiologycategoriesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CardiologyCategoriesID', blank=True, null=True)  # Field name made lowercase.
    cardiologysiteid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CardiologySiteID', related_name='cardiologyexaminations_cardiologysiteid_set', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardiologyExaminations'


class Cardiologyreports(models.Model):
    visitno = models.OneToOneField('Items', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCode', related_name='cardiologyreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCategoryID', related_name='cardiologyreports_itemcategoryid_set')  # Field name made lowercase.
    examdatetime = models.DateTimeField(db_column='ExamDateTime', blank=True, null=True)  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    cardiologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Cardiologist', blank=True, null=True)  # Field name made lowercase.
    cardiologytitleid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CardiologyTitleID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CardiologyReports'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Childgrowth(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    socialsmile = models.BooleanField(db_column='SocialSmile', blank=True, null=True)  # Field name made lowercase.
    headcontrol = models.BooleanField(db_column='HeadControl', blank=True, null=True)  # Field name made lowercase.
    reactiontosound = models.BooleanField(db_column='ReactionToSound', blank=True, null=True)  # Field name made lowercase.
    graspreflex = models.BooleanField(db_column='GraspReflex', blank=True, null=True)  # Field name made lowercase.
    sitting = models.BooleanField(db_column='Sitting', blank=True, null=True)  # Field name made lowercase.
    standing = models.BooleanField(db_column='Standing', blank=True, null=True)  # Field name made lowercase.
    weightforage = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WeightForAge', blank=True, null=True)  # Field name made lowercase.
    heightforage = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HeightForAge', related_name='childgrowth_heightforage_set', blank=True, null=True)  # Field name made lowercase.
    weightforheight = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WeightForHeight', related_name='childgrowth_weightforheight_set', blank=True, null=True)  # Field name made lowercase.
    breastfeedingid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BreastFeedingID', related_name='childgrowth_breastfeedingid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChildGrowth'


class Childnutrition(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    breastfeeding = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BreastFeeding', blank=True, null=True)  # Field name made lowercase.
    ifnodetails = models.CharField(db_column='IfNoDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    complementaryfoods = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ComplementaryFoods', related_name='childnutrition_complementaryfoods_set', blank=True, null=True)  # Field name made lowercase.
    complementaryfoodsdetails = models.CharField(db_column='ComplementaryFoodsDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChildNutrition'


class Claimdetails(models.Model):
    claimno = models.OneToOneField('Claims', models.DO_NOTHING, db_column='ClaimNo', primary_key=True)  # Field name made lowercase. The composite primary key (ClaimNo, ItemName) found, that is not supported. The first column is selected.
    itemname = models.CharField(db_column='ItemName', max_length=100)  # Field name made lowercase.
    benefitcode = models.ForeignKey('Memberbenefits', models.DO_NOTHING, db_column='BenefitCode', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adjustment = models.DecimalField(db_column='Adjustment', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=400, blank=True, null=True)  # Field name made lowercase.
    limitamount = models.DecimalField(db_column='LimitAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumedamount = models.DecimalField(db_column='ConsumedAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    limitbalance = models.DecimalField(db_column='LimitBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClaimDetails'
        unique_together = (('claimno', 'itemname'),)


class Claimdiagnosis(models.Model):
    claimno = models.OneToOneField('Claims', models.DO_NOTHING, db_column='ClaimNo', primary_key=True)  # Field name made lowercase. The composite primary key (ClaimNo, DiseaseCode) found, that is not supported. The first column is selected.
    diseasecode = models.ForeignKey('Diseases', models.DO_NOTHING, db_column='DiseaseCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClaimDiagnosis'
        unique_together = (('claimno', 'diseasecode'),)


class Claimpayments(models.Model):
    claimno = models.OneToOneField('Claims', models.DO_NOTHING, db_column='ClaimNo', primary_key=True)  # Field name made lowercase.
    paystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayStatusID', blank=True, null=True)  # Field name made lowercase.
    paymentdatetime = models.DateTimeField(db_column='PaymentDateTime', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClaimPayments'
        unique_together = (('claimno', 'paystatusid', 'paymentdatetime'),)


class Claims(models.Model):
    claimid = models.IntegerField(db_column='ClaimID')  # Field name made lowercase.
    claimno = models.CharField(db_column='ClaimNo', primary_key=True, max_length=20)  # Field name made lowercase.
    medicalcardno = models.ForeignKey('Schememembers', models.DO_NOTHING, db_column='MedicalCardNo', blank=True, null=True)  # Field name made lowercase.
    patientno = models.CharField(db_column='PatientNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    visitdate = models.DateTimeField(db_column='VisitDate', blank=True, null=True)  # Field name made lowercase.
    visittime = models.CharField(db_column='VisitTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    healthunitcode = models.ForeignKey('Healthunits', models.DO_NOTHING, db_column='HealthUnitCode', blank=True, null=True)  # Field name made lowercase.
    primarydoctor = models.CharField(db_column='PrimaryDoctor', max_length=41, blank=True, null=True)  # Field name made lowercase.
    claimstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ClaimStatusID', blank=True, null=True)  # Field name made lowercase.
    claimentryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ClaimEntryID', related_name='claims_claimentryid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Claims'


class Claimsext(models.Model):
    claimno = models.OneToOneField(Claims, models.DO_NOTHING, db_column='ClaimNo', primary_key=True)  # Field name made lowercase.
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClaimsEXT'


class Clients(models.Model):
    referenceid = models.IntegerField(db_column='ReferenceID', blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='GenderID', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DoctorSpecialtyID', related_name='clients_doctorspecialtyid_set', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    appointmentdate = models.DateTimeField(db_column='AppointmentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clients'


class Clinicaldocs(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase. The composite primary key (ObjectName, ObjectNo, DocNo) found, that is not supported. The first column is selected.
    objectno = models.CharField(db_column='ObjectNo', max_length=20)  # Field name made lowercase.
    docno = models.AutoField(primary_key=True, db_column='DocNo')  # Field name made lowercase.
    docname = models.CharField(db_column='DocName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    clinicaldoc = models.BinaryField(db_column='ClinicalDoc', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicalDocs'
        unique_together = (('objectname', 'objectno', 'docno'),)


class Clinicalfindingimages(models.Model):
    visitno = models.CharField(db_column='VisitNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (VisitNo, ImageName) found, that is not supported. The first column is selected.
    imagename = models.CharField(db_column='ImageName', max_length=40)  # Field name made lowercase.
    clinicalimage = models.BinaryField(db_column='ClinicalImage', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicalFindingImages'
        unique_together = (('visitno', 'imagename'),)


class Clinicalfindings(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    presentingcomplaint = models.CharField(db_column='PresentingComplaint', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    clinicalnotes = models.CharField(db_column='ClinicalNotes', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    ros = models.CharField(db_column='ROS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pmh = models.CharField(db_column='PMH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    poh = models.CharField(db_column='POH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pgh = models.CharField(db_column='PGH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fsh = models.CharField(db_column='FSH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    generalappearance = models.CharField(db_column='GeneralAppearance', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    respiratory = models.CharField(db_column='Respiratory', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cvs = models.CharField(db_column='CVS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ent = models.CharField(db_column='ENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    abdomen = models.CharField(db_column='Abdomen', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    cns = models.CharField(db_column='CNS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    eye = models.CharField(db_column='EYE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    muscularskeletal = models.CharField(db_column='MuscularSkeletal', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    skin = models.CharField(db_column='Skin', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pv = models.CharField(db_column='PV', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    psychologicalstatus = models.CharField(db_column='PsychologicalStatus', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(db_column='ProvisionalDiagnosis', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    treatmentplan = models.CharField(db_column='TreatmentPlan', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicalFindings'


class Clinicalimages(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase. The composite primary key (ObjectName, ObjectNo, ImageNo) found, that is not supported. The first column is selected.
    objectno = models.CharField(db_column='ObjectNo', max_length=20)  # Field name made lowercase.
    imageno = models.AutoField(primary_key=True, db_column='ImageNo')  # Field name made lowercase.
    imagename = models.CharField(db_column='ImageName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    image = models.BinaryField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClinicalImages'
        unique_together = (('objectname', 'objectno', 'imageno'),)


class Companies(models.Model):
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    companyno = models.CharField(db_column='CompanyNo', primary_key=True, max_length=20)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', unique=True, max_length=60, blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contractstartdate = models.DateTimeField(db_column='ContractStartDate', blank=True, null=True)  # Field name made lowercase.
    contractenddate = models.DateTimeField(db_column='ContractEndDate', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Companies'


class Consumableitems(models.Model):
    consumableid = models.IntegerField(db_column='ConsumableID')  # Field name made lowercase.
    consumableno = models.CharField(db_column='ConsumableNo', primary_key=True, max_length=20)  # Field name made lowercase.
    consumablename = models.CharField(db_column='ConsumableName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    alternatename = models.CharField(db_column='AlternateName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unitmeasureid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='UnitMeasureID', blank=True, null=True)  # Field name made lowercase.
    consumablecategoryid = models.CharField(db_column='ConsumableCategoryID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    orderlevel = models.IntegerField(db_column='OrderLevel', blank=True, null=True)  # Field name made lowercase.
    keepingunit = models.IntegerField(db_column='KeepingUnit', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    halted = models.BooleanField(db_column='Halted', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitsinstock = models.IntegerField(db_column='UnitsInStock', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsumableItems'


class Contraceptiveshistory(models.Model):
    patientno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientNo')  # Field name made lowercase.
    contraceptiveid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ContraceptiveID')  # Field name made lowercase.
    complicationdetails = models.CharField(db_column='ComplicationDetails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datestarted = models.DateTimeField(db_column='DateStarted', blank=True, null=True)  # Field name made lowercase.
    discontinuedremovedid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DiscontinuedRemovedID', related_name='contraceptiveshistory_discontinuedremovedid_set', blank=True, null=True)  # Field name made lowercase.
    removalreasonsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RemovalReasonsID', related_name='contraceptiveshistory_removalreasonsid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    ancno = models.OneToOneField(Antenatalenrollment, models.DO_NOTHING, db_column='ANCNo', primary_key=True)  # Field name made lowercase. The composite primary key (ANCNo, ContraceptiveID) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'ContraceptivesHistory'
        unique_together = (('ancno', 'contraceptiveid'),)


class Counties(models.Model):
    countycode = models.CharField(db_column='CountyCode', primary_key=True, max_length=20)  # Field name made lowercase.
    countyname = models.CharField(db_column='CountyName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    districtsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DistrictsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Counties'
        unique_together = (('countyname', 'districtsid'),)


class Deaths(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase.
    deathdate = models.DateTimeField(db_column='DeathDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    staffno = models.CharField(db_column='StaffNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeofdeath = models.CharField(db_column='TimeOfDeath', max_length=8, blank=True, null=True)  # Field name made lowercase.
    primarycauseofdeath = models.CharField(db_column='PrimaryCauseOfDeath', max_length=200, blank=True, null=True)  # Field name made lowercase.
    secondarycauseofdeath = models.CharField(db_column='SecondaryCauseOfDeath', max_length=200, blank=True, null=True)  # Field name made lowercase.
    othercauseofdeath = models.CharField(db_column='OtherCauseOfDeath', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Deaths'


class Deliverynotedetails(models.Model):
    transferno = models.CharField(db_column='TransferNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (TransferNo, ItemCategoryID, ItemCode, BatchNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.CharField(db_column='ItemCategoryID', max_length=10)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    packid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PackID', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    packsize = models.IntegerField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeliveryNoteDetails'
        unique_together = (('transferno', 'itemcategoryid', 'itemcode', 'batchno'),)


class Dentalreports(models.Model):
    visitno = models.OneToOneField('Items', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCode', related_name='dentalreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCategoryID', related_name='dentalreports_itemcategoryid_set')  # Field name made lowercase.
    reportdate = models.DateTimeField(db_column='ReportDate', blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DentalReports'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Dentalservices(models.Model):
    dentalid = models.IntegerField(db_column='DentalID')  # Field name made lowercase.
    dentalcode = models.CharField(db_column='DentalCode', primary_key=True, max_length=10)  # Field name made lowercase.
    dentalname = models.CharField(db_column='DentalName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    dentalcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DentalCategoryID', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DentalServices'


class Depositsint(models.Model):
    transno = models.CharField(db_column='TransNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (TransNo, AgentID) found, that is not supported. The first column is selected.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentID', max_length=20)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepositsINT'
        unique_together = (('transno', 'agentid'),)


class Diagnosis(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName', primary_key=True)  # Field name made lowercase. The composite primary key (ObjectName, TreatmentNo, DiseaseCode) found, that is not supported. The first column is selected.
    treatmentno = models.CharField(db_column='TreatmentNo', max_length=20)  # Field name made lowercase.
    diseasecode = models.ForeignKey('Diseases', models.DO_NOTHING, db_column='DiseaseCode')  # Field name made lowercase.
    diseasename = models.CharField(db_column='DiseaseName', max_length=800, blank=True, null=True)  # Field name made lowercase.
    diseasecategory = models.CharField(db_column='DiseaseCategory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    actionpointid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ActionPointID', blank=True, null=True)  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', related_name='diagnosis_visittypeid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diagnosis'
        unique_together = (('objectname', 'treatmentno', 'diseasecode'),)


class Dimensions(models.Model):
    dimensioncode = models.CharField(db_column='DimensionCode', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (DimensionCode, DimensionTypeID) found, that is not supported. The first column is selected.
    dimensiontypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DimensionTypeID')  # Field name made lowercase.
    dimensionname = models.CharField(db_column='DimensionName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blocked = models.BooleanField(db_column='Blocked', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dimensions'
        unique_together = (('dimensioncode', 'dimensiontypeid'),)


class Discharges(models.Model):
    admissionno = models.OneToOneField(Admissions, models.DO_NOTHING, db_column='AdmissionNo', primary_key=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    roundno = models.ForeignKey('Ipddoctor', models.DO_NOTHING, db_column='RoundNo', blank=True, null=True)  # Field name made lowercase.
    dischargedatetime = models.DateTimeField(db_column='DischargeDateTime', blank=True, null=True)  # Field name made lowercase.
    dischargenotes = models.CharField(db_column='DischargeNotes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    dischargestatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DischargeStatusID', blank=True, null=True)  # Field name made lowercase.
    reviewdate = models.DateTimeField(db_column='ReviewDate', blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=400, blank=True, null=True)  # Field name made lowercase.
    examination = models.CharField(db_column='Examination', max_length=400, blank=True, null=True)  # Field name made lowercase.
    keyfindingsinvestigation = models.CharField(db_column='KeyFindingsInvestigation', max_length=400, blank=True, null=True)  # Field name made lowercase.
    treatmentplan = models.CharField(db_column='TreatmentPlan', max_length=400, blank=True, null=True)  # Field name made lowercase.
    outcomeoftreatment = models.CharField(db_column='OutcomeOfTreatment', max_length=400, blank=True, null=True)  # Field name made lowercase.
    keyrecommendations = models.CharField(db_column='KeyRecommendations', max_length=400, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    dischargewardid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DischargeWardID', related_name='discharges_dischargewardid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Discharges'


class Diseases(models.Model):
    diseasecode = models.CharField(db_column='DiseaseCode', primary_key=True, max_length=10)  # Field name made lowercase.
    diseasename = models.CharField(db_column='DiseaseName', unique=True, max_length=800, blank=True, null=True)  # Field name made lowercase.
    diseasecategoriesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DiseaseCategoriesID', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diseases'


class Diseasesext(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=10)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=800, blank=True, null=True)  # Field name made lowercase.
    reporttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReportTypeID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiseasesEXT'


class Dispenseverification(models.Model):
    visitno = models.OneToOneField('Items', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCode', related_name='dispenseverification_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCategoryID', related_name='dispenseverification_itemcategoryid_set')  # Field name made lowercase.
    verificationdatetime = models.DateTimeField(db_column='VerificationDateTime', blank=True, null=True)  # Field name made lowercase.
    pharmacist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Pharmacist', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    served = models.BooleanField(db_column='Served', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispenseVerification'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Dispenseverificationdetails(models.Model):
    visitno = models.OneToOneField(Dispenseverification, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID, BatchNo) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Dispenseverification, models.DO_NOTHING, db_column='ItemCode', related_name='dispenseverificationdetails_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Dispenseverification, models.DO_NOTHING, db_column='ItemCategoryID', related_name='dispenseverificationdetails_itemcategoryid_set')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    dispensedate = models.DateTimeField(db_column='DispenseDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DispenseVerificationDetails'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid', 'batchno'),)


class Doctorvisits(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    servicecode = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceCode', blank=True, null=True)  # Field name made lowercase.
    closed = models.BooleanField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DoctorVisits'


class Drugadministration(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, TakenDateTime, ItemCode) found, that is not supported. The first column is selected.
    takendatetime = models.DateTimeField(db_column='TakenDateTime')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategory = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategory', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    quantitytaken = models.IntegerField(db_column='QuantityTaken', blank=True, null=True)  # Field name made lowercase.
    nursenotes = models.CharField(db_column='NurseNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrugAdministration'
        unique_together = (('visitno', 'takendatetime', 'itemcode'), ('visitno', 'takendatetime', 'itemname'),)


class Drugcategories(models.Model):
    categoryno = models.CharField(db_column='CategoryNo', primary_key=True, max_length=10)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    varyprescribedqty = models.BooleanField(db_column='VaryPrescribedQty', blank=True, null=True)  # Field name made lowercase.
    defaultprescribedqty = models.SmallIntegerField(db_column='DefaultPrescribedQty', blank=True, null=True)  # Field name made lowercase.
    dosageseparator = models.CharField(db_column='DosageSeparator', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dosagecalculationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DosageCalculationID', blank=True, null=True)  # Field name made lowercase.
    dosageformat = models.CharField(db_column='DosageFormat', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrugCategories'


class Drugcombinationdetails(models.Model):
    combination = models.OneToOneField('Drugcombinations', models.DO_NOTHING, db_column='Combination', primary_key=True)  # Field name made lowercase. The composite primary key (Combination, DrugNo) found, that is not supported. The first column is selected.
    drugno = models.ForeignKey('Drugs', models.DO_NOTHING, db_column='DrugNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrugCombinationDetails'
        unique_together = (('combination', 'drugno'),)


class Drugcombinations(models.Model):
    combination = models.CharField(db_column='Combination', primary_key=True, max_length=30)  # Field name made lowercase.
    combinationdes = models.CharField(db_column='CombinationDes', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrugCombinations'


class Drugs(models.Model):
    drugid = models.IntegerField(db_column='DrugID')  # Field name made lowercase.
    drugno = models.CharField(db_column='DrugNo', primary_key=True, max_length=20)  # Field name made lowercase.
    drugname = models.CharField(db_column='DrugName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    alternatename = models.CharField(db_column='AlternateName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    categoryno = models.ForeignKey(Drugcategories, models.DO_NOTHING, db_column='CategoryNo', blank=True, null=True)  # Field name made lowercase.
    groupsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='GroupsID', blank=True, null=True)  # Field name made lowercase.
    unitmeasureid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='UnitMeasureID', related_name='drugs_unitmeasureid_set', blank=True, null=True)  # Field name made lowercase.
    orderlevel = models.IntegerField(db_column='OrderLevel', blank=True, null=True)  # Field name made lowercase.
    keepingunit = models.IntegerField(db_column='KeepingUnit', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    halted = models.BooleanField(db_column='Halted', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitsinstock = models.IntegerField(db_column='UnitsInStock', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Drugs'


class Enrollmentinformation(models.Model):
    uciid = models.OneToOneField('Researchroutingform', models.DO_NOTHING, db_column='UCIID', primary_key=True)  # Field name made lowercase. The composite primary key (UCIID, ReferralStudyCodeID) found, that is not supported. The first column is selected.
    referralstudycodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReferralStudyCodeID')  # Field name made lowercase.
    enrolledid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EnrolledID', related_name='enrollmentinformation_enrolledid_set', blank=True, null=True)  # Field name made lowercase.
    coenrolledid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoEnrolledID', related_name='enrollmentinformation_coenrolledid_set', blank=True, null=True)  # Field name made lowercase.
    coenrolledstudycodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoEnrolledStudyCodeID', related_name='enrollmentinformation_coenrolledstudycodeid_set', blank=True, null=True)  # Field name made lowercase.
    ccinitials = models.CharField(db_column='CCInitials', max_length=20, blank=True, null=True)  # Field name made lowercase.
    exclusionreason = models.CharField(db_column='ExclusionReason', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    enrollmentdate = models.DateTimeField(db_column='EnrollmentDate', blank=True, null=True)  # Field name made lowercase.
    patientreferred = models.CharField(db_column='PatientReferred', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    referreddate = models.DateTimeField(db_column='ReferredDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EnrollmentInformation'
        unique_together = (('uciid', 'referralstudycodeid'),)


class Examinations(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    examvisittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ExamVisitTypeID', blank=True, null=True)  # Field name made lowercase.
    followupdate = models.DateTimeField(db_column='FollowupDate', blank=True, null=True)  # Field name made lowercase.
    durationstartart = models.IntegerField(db_column='DurationStartART', blank=True, null=True)  # Field name made lowercase.
    durationcurrentart = models.IntegerField(db_column='DurationCurrentART', blank=True, null=True)  # Field name made lowercase.
    oedemaid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='OedemaID', related_name='examinations_oedemaid_set', blank=True, null=True)  # Field name made lowercase.
    pregnancystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PregnancyStatusID', related_name='examinations_pregnancystatusid_set', blank=True, null=True)  # Field name made lowercase.
    expecteddeliverydate = models.DateTimeField(db_column='ExpectedDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    pmtct = models.BooleanField(db_column='PMTCT', blank=True, null=True)  # Field name made lowercase.
    gestationalage = models.SmallIntegerField(db_column='GestationalAge', blank=True, null=True)  # Field name made lowercase.
    muacstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='MUACStatusID', related_name='examinations_muacstatusid_set', blank=True, null=True)  # Field name made lowercase.
    fpmethods = models.CharField(db_column='FPMethods', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tbstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TBStatusID', related_name='examinations_tbstatusid_set', blank=True, null=True)  # Field name made lowercase.
    tbrxstartdate = models.DateTimeField(db_column='TBRxStartDate', blank=True, null=True)  # Field name made lowercase.
    tbrxstopdate = models.DateTimeField(db_column='TBRxStopDate', blank=True, null=True)  # Field name made lowercase.
    tbregno = models.CharField(db_column='TBRegNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sideeffects = models.CharField(db_column='SideEffects', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newoi = models.CharField(db_column='NewOI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    functionalstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='FunctionalStatusID', related_name='examinations_functionalstatusid_set', blank=True, null=True)  # Field name made lowercase.
    whostageid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WHOStageID', related_name='examinations_whostageid_set', blank=True, null=True)  # Field name made lowercase.
    cptadhereid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CPTAdhereID', related_name='examinations_cptadhereid_set', blank=True, null=True)  # Field name made lowercase.
    cptdosage = models.SmallIntegerField(db_column='CPTDosage', blank=True, null=True)  # Field name made lowercase.
    cptduration = models.SmallIntegerField(db_column='CPTDuration', blank=True, null=True)  # Field name made lowercase.
    othermeds = models.CharField(db_column='OtherMeds', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nutritionalsupid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='NutritionalSupID', related_name='examinations_nutritionalsupid_set', blank=True, null=True)  # Field name made lowercase.
    arvadhereid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ARVAdhereID', related_name='examinations_arvadhereid_set', blank=True, null=True)  # Field name made lowercase.
    arvadherewhy = models.CharField(db_column='ARVAdhereWhy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    combination = models.ForeignKey(Drugcombinations, models.DO_NOTHING, db_column='Combination', blank=True, null=True)  # Field name made lowercase.
    arvdosage = models.SmallIntegerField(db_column='ARVDosage', blank=True, null=True)  # Field name made lowercase.
    arvduration = models.SmallIntegerField(db_column='ARVDuration', blank=True, null=True)  # Field name made lowercase.
    cd4abs = models.DecimalField(db_column='CD4ABS', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cd4pct = models.DecimalField(db_column='CD4PCT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    investigations = models.CharField(db_column='Investigations', max_length=200, blank=True, null=True)  # Field name made lowercase.
    refer = models.CharField(db_column='Refer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dayshosp = models.SmallIntegerField(db_column='DaysHOSP', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Examinations'


class Exchangerates(models.Model):
    currenciesid = models.OneToOneField('Lookupdata', models.DO_NOTHING, db_column='CurrenciesID', primary_key=True)  # Field name made lowercase.
    buying = models.DecimalField(db_column='Buying', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    selling = models.DecimalField(db_column='Selling', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExchangeRates'


class Expenditure(models.Model):
    expenditureid = models.IntegerField(db_column='ExpenditureID')  # Field name made lowercase.
    expenditureno = models.CharField(db_column='ExpenditureNo', primary_key=True, max_length=20)  # Field name made lowercase.
    spentdate = models.DateTimeField(db_column='SpentDate', blank=True, null=True)  # Field name made lowercase.
    expenditurecategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ExpenditureCategoryID', blank=True, null=True)  # Field name made lowercase.
    expendituresourcetypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ExpenditureSourceTypeID', related_name='expenditure_expendituresourcetypeid_set', blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    givento = models.CharField(db_column='GivenTo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=100, blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BranchID', related_name='expenditure_branchid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Expenditure'


class Exposedinfants(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, InfantName) found, that is not supported. The first column is selected.
    infantname = models.CharField(db_column='InfantName', max_length=41)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    infantfeedingid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='InfantFeedingID', blank=True, null=True)  # Field name made lowercase.
    ctxstarted = models.CharField(db_column='CTXStarted', max_length=41, blank=True, null=True)  # Field name made lowercase.
    hivtesttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVTestTypeID', related_name='exposedinfants_hivtesttypeid_set', blank=True, null=True)  # Field name made lowercase.
    testresultsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TestResultsID', related_name='exposedinfants_testresultsid_set', blank=True, null=True)  # Field name made lowercase.
    infantstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='InfantStatusID', related_name='exposedinfants_infantstatusid_set', blank=True, null=True)  # Field name made lowercase.
    uniqueno = models.CharField(db_column='UniqueNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExposedInfants'
        unique_together = (('patientno', 'infantname'),)


class Externalreferrals(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    procedurepaidby = models.CharField(db_column='ProcedurePaidBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    employeename = models.CharField(db_column='EmployeeName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referredto = models.CharField(db_column='ReferredTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    departuretime = models.CharField(db_column='DepartureTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    dateofreferral = models.DateTimeField(db_column='DateOfReferral', blank=True, null=True)  # Field name made lowercase.
    historyandsymptoms = models.CharField(db_column='HistoryAndSymptoms', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(db_column='Diagnosis', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    treatmentgiven = models.CharField(db_column='TreatmentGiven', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    reasonforreferral = models.CharField(db_column='ReasonForReferral', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    labinvestigations = models.CharField(db_column='LabInvestigations', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    authorisedby = models.CharField(db_column='AuthorisedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    treatmentlimit = models.DecimalField(db_column='TreatmentLimit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternalReferrals'


class Extrabillitemadjustments(models.Model):
    adjustmentno = models.OneToOneField(Billadjustments, models.DO_NOTHING, db_column='AdjustmentNo', primary_key=True)  # Field name made lowercase. The composite primary key (AdjustmentNo, ExtraBillNo, ExtraBillNo, ItemCode, ItemCategoryID, ItemCategoryID) found, that is not supported. The first column is selected.
    extrabillno = models.ForeignKey('Extrabillitems', models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    itemcode = models.ForeignKey('Extrabillitems', models.DO_NOTHING, db_column='ItemCode', related_name='extrabillitemadjustments_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Extrabillitems', models.DO_NOTHING, db_column='ItemCategoryID', related_name='extrabillitemadjustments_itemcategoryid_set')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    entrylevelid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryLevelID', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    acknowledgeable = models.BooleanField(db_column='Acknowledgeable', blank=True, null=True)  # Field name made lowercase.
    isacknowledged = models.BooleanField(db_column='IsAcknowledged', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtraBillItemAdjustments'
        unique_together = (('adjustmentno', 'extrabillno', 'extrabillno', 'itemcode', 'itemcategoryid', 'itemcategoryid'),)


class Extrabillitems(models.Model):
    extrabillno = models.OneToOneField('Extrabills', models.DO_NOTHING, db_column='ExtraBillNo', primary_key=True)  # Field name made lowercase. The composite primary key (ExtraBillNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatvalue = models.DecimalField(db_column='VATValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    paystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayStatusID', related_name='extrabillitems_paystatusid_set', blank=True, null=True)  # Field name made lowercase.
    entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', related_name='extrabillitems_entrymodeid_set', blank=True, null=True)  # Field name made lowercase.
    originalquantity = models.IntegerField(db_column='OriginalQuantity', blank=True, null=True)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='OriginalPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    returnquantity = models.IntegerField(db_column='ReturnQuantity', blank=True, null=True)  # Field name made lowercase.
    returnamount = models.DecimalField(db_column='ReturnAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    creatorloginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='CreatorLoginID', related_name='extrabillitems_creatorloginid_set', blank=True, null=True)  # Field name made lowercase.
    creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    adjustmentcount = models.IntegerField(db_column='AdjustmentCount', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    originalamount = models.DecimalField(db_column='OriginalAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtraBillItems'
        unique_together = (('extrabillno', 'itemcode', 'itemcategoryid'), ('extrabillno', 'itemcategoryid', 'itemcode'),)


class Extrabills(models.Model):
    extrabillid = models.IntegerField(db_column='ExtraBillID')  # Field name made lowercase.
    extrabillno = models.CharField(db_column='ExtraBillNo', primary_key=True, max_length=20)  # Field name made lowercase.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    extrabilldate = models.DateTimeField(db_column='ExtraBillDate', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.
    billmodesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BillModesID', related_name='extrabills_billmodesid_set', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insuranceno = models.CharField(db_column='InsuranceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    associatedbillno = models.ForeignKey(Billcustomers, models.DO_NOTHING, db_column='AssociatedBillNo', blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(db_column='MemberCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mainmembername = models.CharField(db_column='MainMemberName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    claimreferenceno = models.CharField(db_column='ClaimReferenceNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    copaytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoPayTypeID', related_name='extrabills_copaytypeid_set', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    copayvalue = models.DecimalField(db_column='CoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    accesscashservices = models.BooleanField(db_column='AccessCashServices', blank=True, null=True)  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(db_column='SmartCardApplicable', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountpaid = models.DecimalField(db_column='AmountPaid', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayTypeID', related_name='extrabills_paytypeid_set', blank=True, null=True)  # Field name made lowercase.
    associatedextrabillno = models.ForeignKey('self', models.DO_NOTHING, db_column='AssociatedExtraBillNo', blank=True, null=True)  # Field name made lowercase.
    originalamount = models.DecimalField(db_column='OriginalAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtraBills'


class Extrabillsext(models.Model):
    extrabillno = models.OneToOneField(Extrabills, models.DO_NOTHING, db_column='ExtraBillNo', primary_key=True)  # Field name made lowercase.
    roundno = models.ForeignKey('Ipddoctor', models.DO_NOTHING, db_column='RoundNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtraBillsEXT'


class Extrachargeitems(models.Model):
    extraitemid = models.IntegerField(db_column='ExtraItemID')  # Field name made lowercase.
    extraitemcode = models.CharField(db_column='ExtraItemCode', primary_key=True, max_length=20)  # Field name made lowercase.
    extraitemname = models.CharField(db_column='ExtraItemName', unique=True, max_length=800, blank=True, null=True)  # Field name made lowercase.
    extrachargecategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ExtraChargeCategoryID', blank=True, null=True)  # Field name made lowercase.
    revenuestreamcode = models.CharField(db_column='RevenueStreamCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtraChargeItems'


class Eyeassessment(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    leftpupil = models.CharField(db_column='LeftPupil', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightpupil = models.CharField(db_column='RightPupil', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftlidmargin = models.CharField(db_column='LeftLidMargin', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightlidmargin = models.CharField(db_column='RightLidMargin', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftconjuctiva = models.CharField(db_column='LeftConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightconjuctiva = models.CharField(db_column='RightConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftbulbarconjuctiva = models.CharField(db_column='LeftBulbarConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightbulbarconjuctiva = models.CharField(db_column='RightBulbarConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftcentralcornea = models.CharField(db_column='LeftCentralCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightcentralcornea = models.CharField(db_column='RightCentralCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftverticalcornea = models.CharField(db_column='LeftVerticalCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightverticalcornea = models.CharField(db_column='RightVerticalCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftanteriorchamber = models.CharField(db_column='LeftAnteriorChamber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightanteriorchamber = models.CharField(db_column='RightAnteriorChamber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftirish = models.CharField(db_column='LeftIrish', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightirish = models.CharField(db_column='RightIrish', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftanteriorchamberangle = models.CharField(db_column='LeftAnteriorChamberAngle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightanteriorchamberangle = models.CharField(db_column='RightAnteriorChamberAngle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftretina = models.CharField(db_column='LeftRetina', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightretina = models.CharField(db_column='RightRetina', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftmacular = models.CharField(db_column='LeftMacular', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightmacular = models.CharField(db_column='RightMacular', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftopticdisc = models.CharField(db_column='LeftOpticDisc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightopticdisc = models.CharField(db_column='RightOpticDisc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftiop = models.CharField(db_column='LeftIOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rightiop = models.CharField(db_column='RightIOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leftvitreous = models.CharField(db_column='LeftVitreous', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightvitreous = models.CharField(db_column='RightVitreous', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftlense = models.CharField(db_column='LeftLense', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightlense = models.CharField(db_column='RightLense', max_length=200, blank=True, null=True)  # Field name made lowercase.
    eyenotes = models.CharField(db_column='EyeNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lefteyeball = models.CharField(db_column='LeftEyeBall', max_length=200, blank=True, null=True)  # Field name made lowercase.
    righteyeball = models.CharField(db_column='RightEyeBall', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftorbit = models.CharField(db_column='LeftOrbit', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightorbit = models.CharField(db_column='RightOrbit', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EyeAssessment'


class Eyeservices(models.Model):
    eyeid = models.IntegerField(db_column='EyeID')  # Field name made lowercase.
    eyecode = models.CharField(db_column='EyeCode', primary_key=True, max_length=20)  # Field name made lowercase.
    eyename = models.CharField(db_column='EyeName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EyeServices'


class Familymembers(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, MemberName) found, that is not supported. The first column is selected.
    membername = models.CharField(db_column='MemberName', max_length=41)  # Field name made lowercase.
    age = models.SmallIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    hivstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVStatusID', blank=True, null=True)  # Field name made lowercase.
    hivcareid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVCareID', related_name='familymembers_hivcareid_set', blank=True, null=True)  # Field name made lowercase.
    uniqueno = models.CharField(db_column='UniqueNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FamilyMembers'
        unique_together = (('patientno', 'membername'),)


class Goodsreceivednote(models.Model):
    grnid = models.IntegerField(db_column='GRNID')  # Field name made lowercase.
    grnno = models.CharField(db_column='GRNNo', primary_key=True, max_length=20)  # Field name made lowercase.
    purchaseorderno = models.ForeignKey('Purchaseorders', models.DO_NOTHING, db_column='PurchaseOrderNo', blank=True, null=True)  # Field name made lowercase.
    receiveddate = models.DateTimeField(db_column='ReceivedDate', blank=True, null=True)  # Field name made lowercase.
    advicenoteno = models.CharField(db_column='AdviceNoteNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deliverylocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DeliveryLocationID', blank=True, null=True)  # Field name made lowercase.
    discounttotal = models.DecimalField(db_column='DiscountTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvat = models.DecimalField(db_column='TotalVAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BranchID', related_name='goodsreceivednote_branchid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReceivedNote'


class Goodsreceivednotedetailbatches(models.Model):
    grnno = models.OneToOneField('Goodsreceivednotedetails', models.DO_NOTHING, db_column='GRNNo', primary_key=True)  # Field name made lowercase. The composite primary key (GRNNo, GRNNo, ItemCategoryID, ItemCategoryID, ItemCode, BatchNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Goodsreceivednotedetails', models.DO_NOTHING, db_column='ItemCategoryID', related_name='goodsreceivednotedetailbatches_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.ForeignKey('Goodsreceivednotedetails', models.DO_NOTHING, db_column='ItemCode', related_name='goodsreceivednotedetailbatches_itemcode_set')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    batchreceivedquantity = models.IntegerField(db_column='BatchReceivedQuantity', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReceivedNoteDetailBatches'
        unique_together = (('grnno', 'grnno', 'itemcategoryid', 'itemcategoryid', 'itemcode', 'batchno'),)


class Goodsreceivednotedetails(models.Model):
    grnno = models.OneToOneField(Goodsreceivednote, models.DO_NOTHING, db_column='GRNNo', primary_key=True)  # Field name made lowercase. The composite primary key (GRNNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderedquantity = models.IntegerField(db_column='OrderedQuantity', blank=True, null=True)  # Field name made lowercase.
    packid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PackID', related_name='goodsreceivednotedetails_packid_set')  # Field name made lowercase.
    packsize = models.IntegerField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    receivedquantity = models.IntegerField(db_column='ReceivedQuantity', blank=True, null=True)  # Field name made lowercase.
    bonusquantity = models.IntegerField(db_column='BonusQuantity', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatvalue = models.DecimalField(db_column='VATValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayStatusID', related_name='goodsreceivednotedetails_paystatusid_set', blank=True, null=True)  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReceivedNoteDetails'
        unique_together = (('grnno', 'itemcategoryid', 'itemcode'), ('grnno', 'itemcategoryid', 'itemname'),)


class Goodsreturnednote(models.Model):
    returnid = models.IntegerField(db_column='ReturnID', blank=True, null=True)  # Field name made lowercase.
    returnno = models.CharField(db_column='ReturnNo', primary_key=True, max_length=20)  # Field name made lowercase.
    grnno = models.ForeignKey(Goodsreceivednote, models.DO_NOTHING, db_column='GRNNo', blank=True, null=True)  # Field name made lowercase.
    returndate = models.DateTimeField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReturnedNote'


class Goodsreturnednotedetails(models.Model):
    returnno = models.OneToOneField(Goodsreturnednote, models.DO_NOTHING, db_column='ReturnNo', primary_key=True)  # Field name made lowercase. The composite primary key (ReturnNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800, blank=True, null=True)  # Field name made lowercase.
    returnquantity = models.IntegerField(db_column='ReturnQuantity', blank=True, null=True)  # Field name made lowercase.
    goodsreturnreasonid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='GoodsReturnReasonID', related_name='goodsreturnednotedetails_goodsreturnreasonid_set', blank=True, null=True)  # Field name made lowercase.
    sysncstatus = models.BooleanField(db_column='SysncStatus', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReturnedNoteDetails'
        unique_together = (('returnno', 'itemcategoryid', 'itemcode'),)


class Goodsreturnednotedetailsbatches(models.Model):
    returnno = models.OneToOneField(Goodsreturnednotedetails, models.DO_NOTHING, db_column='ReturnNo', primary_key=True)  # Field name made lowercase. The composite primary key (ReturnNo, ReturnNo, ItemCategoryID, ItemCategoryID, ItemCode, BatchNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey(Goodsreturnednotedetails, models.DO_NOTHING, db_column='ItemCategoryID', related_name='goodsreturnednotedetailsbatches_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.ForeignKey(Goodsreturnednotedetails, models.DO_NOTHING, db_column='ItemCode', related_name='goodsreturnednotedetailsbatches_itemcode_set')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    batchreturnquantity = models.IntegerField(db_column='BatchReturnQuantity', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodsReturnedNoteDetailsBatches'
        unique_together = (('returnno', 'returnno', 'itemcategoryid', 'itemcategoryid', 'itemcode', 'batchno'),)


class Hctclientcard(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    districtsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DistrictsID', blank=True, null=True)  # Field name made lowercase.
    healthunitcode = models.ForeignKey('Healthunits', models.DO_NOTHING, db_column='HealthUnitCode')  # Field name made lowercase.
    hsd = models.CharField(db_column='HSD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    centertypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CenterTypeID', related_name='hctclientcard_centertypeid_set')  # Field name made lowercase.
    testingpointid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TestingPointID', related_name='hctclientcard_testingpointid_set')  # Field name made lowercase.
    accompaniedbyid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccompaniedByID', related_name='hctclientcard_accompaniedbyid_set', blank=True, null=True)  # Field name made lowercase.
    pretestcounselingid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PreTestCounselingID', related_name='hctclientcard_pretestcounselingid_set')  # Field name made lowercase.
    counseledasid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CounseledAsID', related_name='hctclientcard_counseledasid_set', blank=True, null=True)  # Field name made lowercase.
    hctentrypoint = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HCTEntryPoint', related_name='hctclientcard_hctentrypoint_set')  # Field name made lowercase.
    maritalstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='MaritalStatusID', related_name='hctclientcard_maritalstatusid_set')  # Field name made lowercase.
    sexualpatnerno = models.SmallIntegerField(db_column='SexualPatnerNo', blank=True, null=True)  # Field name made lowercase.
    testedhivbeforeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TestedHIVBeforeID', related_name='hctclientcard_testedhivbeforeid_set')  # Field name made lowercase.
    hivtestthreemonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVTestThreeMonthsID', related_name='hctclientcard_hivtestthreemonthsid_set', blank=True, null=True)  # Field name made lowercase.
    hivtestsixmonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVTestSixMonthsID', related_name='hctclientcard_hivtestsixmonthsid_set', blank=True, null=True)  # Field name made lowercase.
    hivtesttwelvemonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVTestTwelveMonthsID', related_name='hctclientcard_hivtesttwelvemonthsid_set', blank=True, null=True)  # Field name made lowercase.
    resultthreemonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultThreeMonthsID', related_name='hctclientcard_resultthreemonthsid_set', blank=True, null=True)  # Field name made lowercase.
    resultsixmonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultSixMonthsID', related_name='hctclientcard_resultsixmonthsid_set', blank=True, null=True)  # Field name made lowercase.
    resulttwelvemonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultTwelveMonthsID', related_name='hctclientcard_resulttwelvemonthsid_set', blank=True, null=True)  # Field name made lowercase.
    notestsintwelvemonthsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='NoTestsInTwelveMonthsID', related_name='hctclientcard_notestsintwelvemonthsid_set', blank=True, null=True)  # Field name made lowercase.
    patnertestedhivid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PatnerTestedHIVID', related_name='hctclientcard_patnertestedhivid_set', blank=True, null=True)  # Field name made lowercase.
    patnertypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PatnerTypeID', related_name='hctclientcard_patnertypeid_set', blank=True, null=True)  # Field name made lowercase.
    patnerresultid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PatnerResultID', related_name='hctclientcard_patnerresultid_set', blank=True, null=True)  # Field name made lowercase.
    knowaboutserviceid = models.CharField(db_column='KnowAboutServiceID', max_length=200)  # Field name made lowercase.
    consentid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ConsentID', related_name='hctclientcard_consentid_set')  # Field name made lowercase.
    noconsentreasonid = models.CharField(db_column='NoConsentReasonID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hivresultid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='HIVResultID', related_name='hctclientcard_hivresultid_set', blank=True, null=True)  # Field name made lowercase.
    testdoneby = models.CharField(db_column='TestDoneBy', max_length=41, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    testdate = models.DateTimeField(db_column='TestDate', blank=True, null=True)  # Field name made lowercase.
    resultreceivedid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultReceivedID', related_name='hctclientcard_resultreceivedid_set', blank=True, null=True)  # Field name made lowercase.
    resultreceivedascoupleid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultReceivedAsCoupleID', related_name='hctclientcard_resultreceivedascoupleid_set', blank=True, null=True)  # Field name made lowercase.
    coupleresultsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoupleResultsID', related_name='hctclientcard_coupleresultsid_set', blank=True, null=True)  # Field name made lowercase.
    tbsuspicionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TBSuspicionID', related_name='hctclientcard_tbsuspicionid_set', blank=True, null=True)  # Field name made lowercase.
    stiid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='STIID', related_name='hctclientcard_stiid_set', blank=True, null=True)  # Field name made lowercase.
    startedcotrimoxazoleid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StartedCotrimoxazoleID', related_name='hctclientcard_startedcotrimoxazoleid_set', blank=True, null=True)  # Field name made lowercase.
    linkedtocareid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LinkedToCareID', related_name='hctclientcard_linkedtocareid_set', blank=True, null=True)  # Field name made lowercase.
    wherelinkedtocareid = models.ForeignKey('Healthunits', models.DO_NOTHING, db_column='WhereLinkedToCareID', related_name='hctclientcard_wherelinkedtocareid_set', blank=True, null=True)  # Field name made lowercase.
    referralreason = models.CharField(db_column='ReferralReason', max_length=200, blank=True, null=True)  # Field name made lowercase.
    counselorname = models.CharField(db_column='CounselorName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    counseldate = models.DateTimeField(db_column='CounselDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HCTClientCard'


class Hivcare(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase.
    healthunitcode = models.ForeignKey('Healthunits', models.DO_NOTHING, db_column='HealthUnitCode', blank=True, null=True)  # Field name made lowercase.
    teamleader = models.ForeignKey('Staff', models.DO_NOTHING, db_column='TeamLeader', blank=True, null=True)  # Field name made lowercase.
    ptclinic = models.CharField(db_column='PtClinic', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lc1 = models.CharField(db_column='LC1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    confirmedtestdate = models.DateTimeField(db_column='ConfirmedTestDate', blank=True, null=True)  # Field name made lowercase.
    hivenrolleddate = models.DateTimeField(db_column='HIVEnrolledDate', blank=True, null=True)  # Field name made lowercase.
    eligibleartdate = models.DateTimeField(db_column='EligibleARTDate', blank=True, null=True)  # Field name made lowercase.
    eligiblereadydate = models.DateTimeField(db_column='EligibleReadyDate', blank=True, null=True)  # Field name made lowercase.
    ab = models.BooleanField(db_column='Ab', blank=True, null=True)  # Field name made lowercase.
    pcr = models.BooleanField(db_column='PCR', blank=True, null=True)  # Field name made lowercase.
    hivcarewhere = models.CharField(db_column='HIVCareWhere', max_length=41, blank=True, null=True)  # Field name made lowercase.
    hivcaretransferin = models.BooleanField(db_column='HIVCareTransferIn', blank=True, null=True)  # Field name made lowercase.
    transferinfrom = models.CharField(db_column='TransferInFrom', max_length=41, blank=True, null=True)  # Field name made lowercase.
    whostageid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='WHOStageID', blank=True, null=True)  # Field name made lowercase.
    cd4 = models.DecimalField(db_column='CD4', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    presumptivehiv = models.BooleanField(db_column='PresumptiveHIV', blank=True, null=True)  # Field name made lowercase.
    pcrinfant = models.BooleanField(db_column='PCRInfant', blank=True, null=True)  # Field name made lowercase.
    medicalconditions = models.CharField(db_column='MedicalConditions', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    cohortmonth = models.SmallIntegerField(db_column='COHORTMonth', blank=True, null=True)  # Field name made lowercase.
    cohortyear = models.SmallIntegerField(db_column='COHORTYear', blank=True, null=True)  # Field name made lowercase.
    arttransferindate = models.DateTimeField(db_column='ARTTransferInDate', blank=True, null=True)  # Field name made lowercase.
    arttransferinfrom = models.CharField(db_column='ARTTransferInFrom', max_length=40, blank=True, null=True)  # Field name made lowercase.
    transferinregimen = models.ForeignKey(Drugcombinations, models.DO_NOTHING, db_column='TransferInRegimen', blank=True, null=True)  # Field name made lowercase.
    startartdate = models.DateTimeField(db_column='StartARTDate', blank=True, null=True)  # Field name made lowercase.
    startartregimen = models.ForeignKey(Drugcombinations, models.DO_NOTHING, db_column='StartARTRegimen', related_name='hivcare_startartregimen_set', blank=True, null=True)  # Field name made lowercase.
    startartweight = models.DecimalField(db_column='StartARTWeight', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    startartwhostageid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StartARTWHOStageID', related_name='hivcare_startartwhostageid_set', blank=True, null=True)  # Field name made lowercase.
    startartcd4 = models.DecimalField(db_column='StartARTCD4', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pregnancystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PregnancyStatusID', related_name='hivcare_pregnancystatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    computername = models.CharField(db_column='ComputerName', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HIVCARE'


class Healthunits(models.Model):
    healthunitcode = models.CharField(db_column='HealthUnitCode', primary_key=True, max_length=10)  # Field name made lowercase.
    healthunitname = models.CharField(db_column='HealthUnitName', unique=True, max_length=41, blank=True, null=True)  # Field name made lowercase.
    districtsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DistrictsID', blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthUnits'


class Icuservices(models.Model):
    icuid = models.IntegerField(db_column='ICUID')  # Field name made lowercase.
    icucode = models.CharField(db_column='ICUCode', primary_key=True, max_length=20)  # Field name made lowercase.
    icuname = models.CharField(db_column='ICUName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ICUServices'


class Intadmissions(models.Model):
    agentno = models.CharField(db_column='AgentNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (AgentNo, AdmissionNo) found, that is not supported. The first column is selected.
    admissionno = models.ForeignKey(Admissions, models.DO_NOTHING, db_column='AdmissionNo')  # Field name made lowercase.
    memberlimit = models.DecimalField(db_column='MemberLimit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTAdmissions'
        unique_together = (('agentno', 'admissionno'),)


class Intagents(models.Model):
    agentno = models.CharField(db_column='AgentNo', primary_key=True, max_length=20)  # Field name made lowercase.
    agentname = models.CharField(db_column='AgentName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    connectionmodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ConnectionModeID', blank=True, null=True)  # Field name made lowercase.
    databasetypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DatabaseTypeID', related_name='intagents_databasetypeid_set', blank=True, null=True)  # Field name made lowercase.
    datasource = models.CharField(db_column='DataSource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbname = models.CharField(db_column='DBName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port', blank=True, null=True)  # Field name made lowercase.
    dbusername = models.CharField(db_column='DBUsername', max_length=40, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTAgents'


class Intextrabillitems(models.Model):
    extrabillno = models.OneToOneField(Extrabillitems, models.DO_NOTHING, db_column='ExtraBillNo', primary_key=True)  # Field name made lowercase. The composite primary key (ExtraBillNo, ItemCategoryID, ItemCode, AgentNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='intextrabillitems_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCode', related_name='intextrabillitems_itemcode_set')  # Field name made lowercase.
    agentno = models.ForeignKey(Intagents, models.DO_NOTHING, db_column='AgentNo')  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTExtraBillItems'
        unique_together = (('extrabillno', 'itemcategoryid', 'itemcode', 'agentno'),)


class Intextrabills(models.Model):
    extrabillno = models.OneToOneField(Extrabills, models.DO_NOTHING, db_column='ExtraBillNo', primary_key=True)  # Field name made lowercase. The composite primary key (ExtraBillNo, AgentNo) found, that is not supported. The first column is selected.
    agentno = models.ForeignKey(Intagents, models.DO_NOTHING, db_column='AgentNo')  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTExtraBills'
        unique_together = (('extrabillno', 'agentno'),)


class Intrefunds(models.Model):
    receiptno = models.CharField(db_column='ReceiptNo', primary_key=True, max_length=20)  # Field name made lowercase.
    syncstatus = models.CharField(db_column='SyncStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.
    agentid = models.CharField(db_column='AgentID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTRefunds'


class Intstocktake(models.Model):
    pscno = models.CharField(db_column='PSCNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (PSCNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.CharField(db_column='ItemCategoryID', max_length=10)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=10, blank=True, null=True)  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INTStockTake'
        unique_together = (('pscno', 'itemcategoryid', 'itemcode'),)


class Ipdalerts(models.Model):
    alertid = models.AutoField(db_column='AlertID', primary_key=True)  # Field name made lowercase.
    alerttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AlertTypeID', blank=True, null=True)  # Field name made lowercase.
    roundno = models.ForeignKey('Ipddoctor', models.DO_NOTHING, db_column='RoundNo', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    sentdate = models.DateTimeField(db_column='SentDate', blank=True, null=True)  # Field name made lowercase.
    senttime = models.CharField(db_column='SentTime', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDAlerts'
        unique_together = (('alerttypeid', 'roundno', 'sentdate'),)


class Ipdcancerdiagnosis(models.Model):
    roundno = models.OneToOneField('Ipddoctor', models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, DiseaseNo) found, that is not supported. The first column is selected.
    diseaseno = models.ForeignKey(Cancerdiseases, models.DO_NOTHING, db_column='DiseaseNo')  # Field name made lowercase.
    topographicalno = models.ForeignKey('Topologysites', models.DO_NOTHING, db_column='TopographicalNo', blank=True, null=True)  # Field name made lowercase.
    basisofdiagnosisid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BasisOfDiagnosisID', blank=True, null=True)  # Field name made lowercase.
    cancerstageid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CancerStageID', related_name='ipdcancerdiagnosis_cancerstageid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDCancerDiagnosis'
        unique_together = (('roundno', 'diseaseno'),)


class Ipdcardiologyreports(models.Model):
    roundno = models.OneToOneField('Ipditems', models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey('Ipditems', models.DO_NOTHING, db_column='ItemCode', related_name='ipdcardiologyreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Ipditems', models.DO_NOTHING, db_column='ItemCategoryID', related_name='ipdcardiologyreports_itemcategoryid_set')  # Field name made lowercase.
    examdatetime = models.DateTimeField(db_column='ExamDateTime', blank=True, null=True)  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    cardiologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Cardiologist', blank=True, null=True)  # Field name made lowercase.
    cardiologytitleid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CardiologyTitleID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDCardiologyReports'
        unique_together = (('roundno', 'itemcode', 'itemcategoryid'),)


class Ipdclinicalfindingimages(models.Model):
    roundno = models.OneToOneField('Ipdclinicalfindings', models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ImageName) found, that is not supported. The first column is selected.
    imagename = models.CharField(db_column='ImageName', max_length=40)  # Field name made lowercase.
    clinicalimage = models.BinaryField(db_column='ClinicalImage', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDClinicalFindingImages'
        unique_together = (('roundno', 'imagename'),)


class Ipdclinicalfindings(models.Model):
    roundno = models.OneToOneField('Ipddoctor', models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pulse = models.SmallIntegerField(db_column='Pulse', blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.CharField(db_column='BloodPressure', max_length=10, blank=True, null=True)  # Field name made lowercase.
    headcircum = models.DecimalField(db_column='HeadCircum', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bodysurfacearea = models.DecimalField(db_column='BodySurfaceArea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clinicalnotes = models.CharField(db_column='ClinicalNotes', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    respiratory = models.CharField(db_column='Respiratory', max_length=100, blank=True, null=True)  # Field name made lowercase.
    generalappearance = models.CharField(db_column='GeneralAppearance', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cvs = models.CharField(db_column='CVS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abdomen = models.CharField(db_column='Abdomen', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cns = models.CharField(db_column='CNS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    muscularskeletal = models.CharField(db_column='MuscularSkeletal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    psychologicalstatus = models.CharField(db_column='PsychologicalStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    clinicaldiagnosis = models.CharField(db_column='ClinicalDiagnosis', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    ros = models.CharField(db_column='ROS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pmh = models.CharField(db_column='PMH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    poh = models.CharField(db_column='POH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pgh = models.CharField(db_column='PGH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fsh = models.CharField(db_column='FSH', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ent = models.CharField(db_column='ENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    eye = models.CharField(db_column='EYE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    skin = models.CharField(db_column='Skin', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pv = models.CharField(db_column='PV', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    treatmentplan = models.CharField(db_column='TreatmentPlan', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    muac = models.DecimalField(db_column='MUAC', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    respirationrate = models.DecimalField(db_column='RespirationRate', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDClinicalFindings'


class Ipddentalreports(models.Model):
    roundno = models.OneToOneField('Ipditems', models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey('Ipditems', models.DO_NOTHING, db_column='ItemCode', related_name='ipddentalreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Ipditems', models.DO_NOTHING, db_column='ItemCategoryID', related_name='ipddentalreports_itemcategoryid_set')  # Field name made lowercase.
    reportdate = models.DateTimeField(db_column='ReportDate', blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDDentalReports'
        unique_together = (('roundno', 'itemcode', 'itemcategoryid'),)


class Ipddiagnosisarchive(models.Model):
    roundno = models.CharField(db_column='RoundNo', max_length=20)  # Field name made lowercase.
    diseasecode = models.CharField(db_column='DiseaseCode', max_length=10)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    actionpointid = models.CharField(db_column='ActionPointID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDDiagnosisArchive'


class Ipddoctor(models.Model):
    roundid = models.IntegerField(db_column='RoundID')  # Field name made lowercase.
    roundno = models.CharField(db_column='RoundNo', primary_key=True, max_length=20)  # Field name made lowercase.
    admissionno = models.ForeignKey(Admissions, models.DO_NOTHING, db_column='AdmissionNo', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    rounddatetime = models.DateTimeField(db_column='RoundDateTime', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDDoctor'


class Ipddrugadministration(models.Model):
    nurseroundno = models.OneToOneField('Ipdnurse', models.DO_NOTHING, db_column='NurseRoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (NurseRoundNo, TakenDateTime, ItemCode) found, that is not supported. The first column is selected.
    takendatetime = models.DateTimeField(db_column='TakenDateTime')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    quantitytaken = models.IntegerField(db_column='QuantityTaken', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    nursenotes = models.CharField(db_column='NurseNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDDrugAdministration'
        unique_together = (('nurseroundno', 'takendatetime', 'itemcode'), ('nurseroundno', 'takendatetime', 'itemname'),)


class Ipdeyeassessment(models.Model):
    roundno = models.OneToOneField(Ipddoctor, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    leftpupil = models.CharField(db_column='LeftPupil', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightpupil = models.CharField(db_column='RightPupil', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftlidmargin = models.CharField(db_column='LeftLidMargin', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightlidmargin = models.CharField(db_column='RightLidMargin', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftconjuctiva = models.CharField(db_column='LeftConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightconjuctiva = models.CharField(db_column='RightConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftbulbarconjuctiva = models.CharField(db_column='LeftBulbarConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightbulbarconjuctiva = models.CharField(db_column='RightBulbarConjuctiva', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftcentralcornea = models.CharField(db_column='LeftCentralCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightcentralcornea = models.CharField(db_column='RightCentralCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftverticalcornea = models.CharField(db_column='LeftVerticalCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightverticalcornea = models.CharField(db_column='RightVerticalCornea', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftanteriorchamber = models.CharField(db_column='LeftAnteriorChamber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightanteriorchamber = models.CharField(db_column='RightAnteriorChamber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftirish = models.CharField(db_column='LeftIrish', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightirish = models.CharField(db_column='RightIrish', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftanteriorchamberangle = models.CharField(db_column='LeftAnteriorChamberAngle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightanteriorchamberangle = models.CharField(db_column='RightAnteriorChamberAngle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftretina = models.CharField(db_column='LeftRetina', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightretina = models.CharField(db_column='RightRetina', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftmacular = models.CharField(db_column='LeftMacular', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightmacular = models.CharField(db_column='RightMacular', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftopticdisc = models.CharField(db_column='LeftOpticDisc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightopticdisc = models.CharField(db_column='RightOpticDisc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftiop = models.CharField(db_column='LeftIOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rightiop = models.CharField(db_column='RightIOP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leftvitreous = models.CharField(db_column='LeftVitreous', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightvitreous = models.CharField(db_column='RightVitreous', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftlense = models.CharField(db_column='LeftLense', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightlense = models.CharField(db_column='RightLense', max_length=200, blank=True, null=True)  # Field name made lowercase.
    eyenotes = models.CharField(db_column='EyeNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lefteyeball = models.CharField(db_column='LeftEyeBall', max_length=200, blank=True, null=True)  # Field name made lowercase.
    righteyeball = models.CharField(db_column='RightEyeBall', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftorbit = models.CharField(db_column='LeftOrbit', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightorbit = models.CharField(db_column='RightOrbit', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDEyeAssessment'


class Ipditems(models.Model):
    roundno = models.OneToOneField(Ipddoctor, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdetails = models.CharField(db_column='ItemDetails', max_length=800, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    itemstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemStatusID', related_name='ipditems_itemstatusid_set', blank=True, null=True)  # Field name made lowercase.
    paystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayStatusID', related_name='ipditems_paystatusid_set', blank=True, null=True)  # Field name made lowercase.
    originalquantity = models.IntegerField(db_column='OriginalQuantity', blank=True, null=True)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='OriginalPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    creatorloginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='CreatorLoginID', related_name='ipditems_creatorloginid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDItems'
        unique_together = (('roundno', 'itemcode', 'itemcategoryid'), ('roundno', 'itemcategoryid', 'itemcode'),)


class Ipditemsext(models.Model):
    roundno = models.OneToOneField(Ipditems, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Ipditems, models.DO_NOTHING, db_column='ItemCode', related_name='ipditemsext_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Ipditems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='ipditemsext_itemcategoryid_set')  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    drquantity = models.IntegerField(db_column='DrQuantity', blank=True, null=True)  # Field name made lowercase.
    issuedatetime = models.DateTimeField(db_column='IssueDateTime', blank=True, null=True)  # Field name made lowercase.
    pharmacist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Pharmacist', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDItemsEXT'
        unique_together = (('roundno', 'itemcode', 'itemcategoryid'),)


class Ipdnurse(models.Model):
    ipdnurseroundid = models.IntegerField(db_column='IPDNurseRoundID')  # Field name made lowercase.
    nurseroundno = models.CharField(db_column='NurseRoundNo', primary_key=True, max_length=20)  # Field name made lowercase.
    roundno = models.ForeignKey(Ipddoctor, models.DO_NOTHING, db_column='RoundNo')  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pulse = models.SmallIntegerField(db_column='Pulse', blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.CharField(db_column='BloodPressure', max_length=10, blank=True, null=True)  # Field name made lowercase.
    headcircum = models.DecimalField(db_column='HeadCircum', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bodysurfacearea = models.DecimalField(db_column='BodySurfaceArea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    respirationrate = models.SmallIntegerField(db_column='RespirationRate', blank=True, null=True)  # Field name made lowercase.
    oxygensaturation = models.DecimalField(db_column='OxygenSaturation', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.SmallIntegerField(db_column='HeartRate', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    nurserounddatetime = models.DateTimeField(db_column='NurseRoundDateTime', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    otherattendingnurse = models.CharField(db_column='OtherAttendingNurse', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDNurse'


class Ipdnurseassessment(models.Model):
    roundno = models.OneToOneField(Ipdnurse, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    complaint = models.CharField(db_column='Complaint', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    etiology = models.CharField(db_column='Etiology', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    signsandsymptoms = models.CharField(db_column='SignsAndSymptoms', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    proposedsolution = models.CharField(db_column='ProposedSolution', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDNurseAssessment'


class Ipdnurseevaluation(models.Model):
    roundno = models.OneToOneField(Ipdnurse, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    nursingcareeffective = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='NursingCareEffective', blank=True, null=True)  # Field name made lowercase.
    proposedmodifications = models.CharField(db_column='ProposedModifications', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    evaluationnotes = models.CharField(db_column='EvaluationNotes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDNurseEvaluation'


class Ipdnursefluids(models.Model):
    nurseroundno = models.OneToOneField(Ipdnurse, models.DO_NOTHING, db_column='NurseRoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (NurseRoundNo, FluidTypeID, FluidCategoryID) found, that is not supported. The first column is selected.
    takendatetime = models.DateTimeField(db_column='TakenDateTime', blank=True, null=True)  # Field name made lowercase.
    fluidtypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='FluidTypeID')  # Field name made lowercase.
    fluidcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='FluidCategoryID', related_name='ipdnursefluids_fluidcategoryid_set')  # Field name made lowercase.
    routeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RouteID', related_name='ipdnursefluids_routeid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    nursenotes = models.CharField(db_column='NurseNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDNurseFluids'
        unique_together = (('nurseroundno', 'fluidtypeid', 'fluidcategoryid'), ('nurseroundno', 'fluidtypeid', 'fluidcategoryid'),)


class Ipdnursingplan(models.Model):
    roundno = models.OneToOneField(Ipdnurse, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    expectedoutcome = models.CharField(db_column='ExpectedOutcome', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    nursingactions = models.CharField(db_column='NursingActions', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    implementation = models.CharField(db_column='Implementation', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDNursingPlan'


class Ipdorthoptics(models.Model):
    roundno = models.OneToOneField(Ipddoctor, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    headposture = models.CharField(db_column='HeadPosture', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fixation = models.CharField(db_column='Fixation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lefthirschberg = models.CharField(db_column='LeftHirschberg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    righthirschberg = models.CharField(db_column='RightHirschberg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    righteom = models.CharField(db_column='RightEOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lefteom = models.CharField(db_column='LeftEOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    covertestid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoverTestID', blank=True, null=True)  # Field name made lowercase.
    leftapctglasses = models.CharField(db_column='LeftAPCTGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightapctglasses = models.CharField(db_column='RightAPCTGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftapctwithoutglasses = models.CharField(db_column='LeftAPCTWithOutGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightapctwithoutglasses = models.CharField(db_column='RightAPCTWithOutGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    correspondence = models.CharField(db_column='Correspondence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prismadaptation = models.CharField(db_column='PrismAdaptation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fusionconvergence = models.CharField(db_column='FusionConvergence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fusiondivergence = models.CharField(db_column='FusionDivergence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fusionrange = models.CharField(db_column='FusionRange', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nearpointofaccommodation = models.CharField(db_column='NearPointOfAccommodation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nearpointofconvergence = models.CharField(db_column='NearPointOfConvergence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orthopticsnotes = models.CharField(db_column='OrthopticsNotes', max_length=400, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    stereopsis = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='Stereopsis', related_name='ipdorthoptics_stereopsis_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDOrthoptics'


class Ipdpackageconsumption(models.Model):
    extrabillno = models.CharField(db_column='ExtraBillNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (ExtraBillNo, PackageNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    packageno = models.ForeignKey('Packages', models.DO_NOTHING, db_column='PackageNo')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    packagevisitno = models.CharField(db_column='PackageVisitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemStatusID', related_name='ipdpackageconsumption_itemstatusid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDPackageConsumption'
        unique_together = (('extrabillno', 'packageno', 'itemcode', 'itemcategoryid'),)


class Ipdpathologyreports(models.Model):
    roundno = models.OneToOneField(Ipditems, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Ipditems, models.DO_NOTHING, db_column='ItemCode', related_name='ipdpathologyreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Ipditems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='ipdpathologyreports_itemcategoryid_set')  # Field name made lowercase.
    reporttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReportTypeID', blank=True, null=True)  # Field name made lowercase.
    examdatetime = models.DateTimeField(db_column='ExamDateTime', blank=True, null=True)  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(db_column='Diagnosis', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    macroscopic = models.CharField(db_column='Macroscopic', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    microscopic = models.CharField(db_column='Microscopic', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    pathologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Pathologist', blank=True, null=True)  # Field name made lowercase.
    pathologytitleid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PathologyTitleID', related_name='ipdpathologyreports_pathologytitleid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDPathologyReports'
        unique_together = (('roundno', 'itemcode', 'itemcategoryid'),)


class Ipdradiologyreports(models.Model):
    roundno = models.OneToOneField(Ipditems, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RoundNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Ipditems, models.DO_NOTHING, db_column='ItemCode', related_name='ipdradiologyreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Ipditems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='ipdradiologyreports_itemcategoryid_set')  # Field name made lowercase.
    examdatetime = models.DateTimeField(db_column='ExamDateTime', blank=True, null=True)  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    radiologist = models.CharField(db_column='Radiologist', max_length=10, blank=True, null=True)  # Field name made lowercase.
    radiologytitleid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RadiologyTitleID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDRadiologyReports'
        unique_together = (('roundno', 'itemcode', 'itemcategoryid'),)


class Ipdstaffpaymentdetails(models.Model):
    paymentvoucherno = models.OneToOneField('Staffpayments', models.DO_NOTHING, db_column='PaymentVoucherNo', primary_key=True)  # Field name made lowercase. The composite primary key (PaymentVoucherNo, VisitNo, ExtraBillNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    roundno = models.CharField(db_column='RoundNo', max_length=20)  # Field name made lowercase.
    extrabillno = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    itemcode = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCode', related_name='ipdstaffpaymentdetails_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='ipdstaffpaymentdetails_itemcategoryid_set')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    approvalstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ApprovalStatusID')  # Field name made lowercase.
    approvalnotes = models.CharField(db_column='ApprovalNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDStaffPaymentDetails'
        unique_together = (('paymentvoucherno', 'visitno', 'extrabillno', 'itemcode', 'itemcategoryid'),)


class Ipdtheatreoperations(models.Model):
    roundno = models.OneToOneField(Ipddoctor, models.DO_NOTHING, db_column='RoundNo', primary_key=True)  # Field name made lowercase.
    operationdatetime = models.DateTimeField(db_column='OperationDateTime', blank=True, null=True)  # Field name made lowercase.
    leadsurgeon = models.ForeignKey('Staff', models.DO_NOTHING, db_column='LeadSurgeon', blank=True, null=True)  # Field name made lowercase.
    othersurgeon = models.CharField(db_column='OtherSurgeon', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leadanaesthetist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='LeadAnaesthetist', related_name='ipdtheatreoperations_leadanaesthetist_set', blank=True, null=True)  # Field name made lowercase.
    otheranaesthetist = models.CharField(db_column='OtherAnaesthetist', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leadnurse = models.ForeignKey('Staff', models.DO_NOTHING, db_column='LeadNurse', related_name='ipdtheatreoperations_leadnurse_set', blank=True, null=True)  # Field name made lowercase.
    othernurse = models.CharField(db_column='OtherNurse', max_length=200, blank=True, null=True)  # Field name made lowercase.
    anaesthesiatype = models.CharField(db_column='AnaesthesiaType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    operationclassid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='OperationClassID', blank=True, null=True)  # Field name made lowercase.
    preoperativediagnosis = models.CharField(db_column='PreoperativeDiagnosis', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    plannedprocedures = models.CharField(db_column='PlannedProcedures', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    postoperativeinstructions = models.CharField(db_column='PostoperativeInstructions', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    anesthesiologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Anesthesiologist', related_name='ipdtheatreoperations_anesthesiologist_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDTheatreOperations'


class Ipdvisionassessment(models.Model):
    varoundid = models.IntegerField(db_column='VARoundID', blank=True, null=True)  # Field name made lowercase.
    admissionno = models.ForeignKey(Admissions, models.DO_NOTHING, db_column='AdmissionNo', blank=True, null=True)  # Field name made lowercase.
    rounddatetime = models.DateTimeField(db_column='RoundDateTime', blank=True, null=True)  # Field name made lowercase.
    varoundno = models.CharField(db_column='VARoundNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (VARoundNo, EyeTestID) found, that is not supported. The first column is selected.
    eyetestid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EyeTestID')  # Field name made lowercase.
    visualacuityrightid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisualAcuityRightID', related_name='ipdvisionassessment_visualacuityrightid_set', blank=True, null=True)  # Field name made lowercase.
    visualacuityrightextid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisualAcuityRightExtID', related_name='ipdvisionassessment_visualacuityrightextid_set', blank=True, null=True)  # Field name made lowercase.
    visualacuityleftid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisualAcuityLeftID', related_name='ipdvisionassessment_visualacuityleftid_set', blank=True, null=True)  # Field name made lowercase.
    visualacuityleftextid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisualAcuityLeftExtID', related_name='ipdvisionassessment_visualacuityleftextid_set', blank=True, null=True)  # Field name made lowercase.
    preferentiallookingrightid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PreferentialLookingRightID', related_name='ipdvisionassessment_preferentiallookingrightid_set', blank=True, null=True)  # Field name made lowercase.
    preferentiallookingleftid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PreferentialLookingLeftID', related_name='ipdvisionassessment_preferentiallookingleftid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IPDVisionAssessment'
        unique_together = (('varoundno', 'eyetestid'),)


class Immunisationvaccines(models.Model):
    immunisationid = models.IntegerField(db_column='ImmunisationID', blank=True, null=True)  # Field name made lowercase.
    immunisationno = models.CharField(db_column='ImmunisationNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    patientno = models.CharField(db_column='PatientNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (PatientNo, VaccineName) found, that is not supported. The first column is selected.
    vaccinename = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VaccineName')  # Field name made lowercase.
    vaccinereceived = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VaccineReceived', related_name='immunisationvaccines_vaccinereceived_set', blank=True, null=True)  # Field name made lowercase.
    dategiven = models.DateTimeField(db_column='DateGiven', blank=True, null=True)  # Field name made lowercase.
    placereceived = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PlaceReceived', related_name='immunisationvaccines_placereceived_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mothersname = models.CharField(db_column='MothersName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uptodate = models.BooleanField(db_column='UpToDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImmunisationVaccines'
        unique_together = (('patientno', 'vaccinename'),)


class Importdatainfo(models.Model):
    itemcode = models.OneToOneField('Labtests', models.DO_NOTHING, db_column='ItemCode', primary_key=True)  # Field name made lowercase. The composite primary key (ItemCode, SourceName, SourceCaption) found, that is not supported. The first column is selected.
    sourcename = models.CharField(db_column='SourceName', max_length=60)  # Field name made lowercase.
    sourcecaption = models.CharField(db_column='SourceCaption', max_length=100)  # Field name made lowercase.
    databasetypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DatabaseTypeID', blank=True, null=True)  # Field name made lowercase.
    connectionmodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ConnectionModeID', related_name='importdatainfo_connectionmodeid_set', blank=True, null=True)  # Field name made lowercase.
    importserver = models.CharField(db_column='ImportServer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    importlogin = models.CharField(db_column='ImportLogin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    importpassword = models.CharField(db_column='ImportPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sp_name = models.CharField(db_column='SP_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImportDataInfo'
        unique_together = (('itemcode', 'sourcename', 'sourcecaption'),)


class Insurancecustomfee(models.Model):
    insuranceno = models.OneToOneField('Insurances', models.DO_NOTHING, db_column='InsuranceNo', primary_key=True)  # Field name made lowercase. The composite primary key (InsuranceNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    customfee = models.DecimalField(db_column='CustomFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrenciesID', related_name='insurancecustomfee_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    requirespayment = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='RequiresPayment', related_name='insurancecustomfee_requirespayment_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceCustomFee'
        unique_together = (('insuranceno', 'itemcode', 'itemcategoryid'),)


class Insuranceexcludeditems(models.Model):
    companyno = models.OneToOneField('Insuranceschemes', models.DO_NOTHING, db_column='CompanyNo', primary_key=True)  # Field name made lowercase. The composite primary key (CompanyNo, PolicyNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    policyno = models.ForeignKey('Insuranceschemes', models.DO_NOTHING, db_column='PolicyNo', related_name='insuranceexcludeditems_policyno_set')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceExcludedItems'
        unique_together = (('companyno', 'policyno', 'itemcode', 'itemcategoryid'),)


class Insuranceexclusions(models.Model):
    insuranceno = models.OneToOneField('Insurances', models.DO_NOTHING, db_column='InsuranceNo', primary_key=True)  # Field name made lowercase. The composite primary key (InsuranceNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceExclusions'
        unique_together = (('insuranceno', 'itemcode', 'itemcategoryid'),)


class Insurancepolicies(models.Model):
    policyid = models.IntegerField(db_column='PolicyID')  # Field name made lowercase.
    policyno = models.CharField(db_column='PolicyNo', primary_key=True, max_length=20)  # Field name made lowercase.
    insuranceno = models.ForeignKey('Insurances', models.DO_NOTHING, db_column='InsuranceNo', blank=True, null=True)  # Field name made lowercase.
    policyname = models.CharField(db_column='PolicyName', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsurancePolicies'


class Insuranceschemes(models.Model):
    companyno = models.OneToOneField(Companies, models.DO_NOTHING, db_column='CompanyNo', primary_key=True)  # Field name made lowercase. The composite primary key (CompanyNo, PolicyNo) found, that is not supported. The first column is selected.
    policyno = models.ForeignKey(Insurancepolicies, models.DO_NOTHING, db_column='PolicyNo')  # Field name made lowercase.
    schemejoindate = models.DateTimeField(db_column='SchemeJoinDate', blank=True, null=True)  # Field name made lowercase.
    schemestartdate = models.DateTimeField(db_column='SchemeStartDate', blank=True, null=True)  # Field name made lowercase.
    schemeenddate = models.DateTimeField(db_column='SchemeEndDate', blank=True, null=True)  # Field name made lowercase.
    copaytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CoPayTypeID', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    copayvalue = models.DecimalField(db_column='CoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    annualpremium = models.DecimalField(db_column='AnnualPremium', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    memberpremium = models.DecimalField(db_column='MemberPremium', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(db_column='SmartCardApplicable', blank=True, null=True)  # Field name made lowercase.
    schemestatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SchemeStatusID', related_name='insuranceschemes_schemestatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    opdcopayvalue = models.DecimalField(db_column='OPDCoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipdcopayvalue = models.DecimalField(db_column='IPDCoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceSchemes'
        unique_together = (('companyno', 'policyno'),)


class Insuranceschemesitemcategorycopay(models.Model):
    companyno = models.OneToOneField(Insuranceschemes, models.DO_NOTHING, db_column='CompanyNo', primary_key=True)  # Field name made lowercase. The composite primary key (CompanyNo, PolicyNo, ItemCategoryID) found, that is not supported. The first column is selected.
    policyno = models.ForeignKey(Insuranceschemes, models.DO_NOTHING, db_column='PolicyNo', related_name='insuranceschemesitemcategorycopay_policyno_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceSchemesItemCategoryCopay'
        unique_together = (('companyno', 'policyno', 'itemcategoryid'),)


class Insuranceschemesvisittypecopay(models.Model):
    companyno = models.OneToOneField(Insuranceschemes, models.DO_NOTHING, db_column='CompanyNo', primary_key=True)  # Field name made lowercase. The composite primary key (CompanyNo, PolicyNo, VisitTypeID) found, that is not supported. The first column is selected.
    policyno = models.ForeignKey(Insuranceschemes, models.DO_NOTHING, db_column='PolicyNo', related_name='insuranceschemesvisittypecopay_policyno_set')  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID')  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceSchemesVisitTypeCopay'
        unique_together = (('companyno', 'policyno', 'visittypeid'),)


class Insurancevisittypecustomfee(models.Model):
    insuranceno = models.OneToOneField('Insurances', models.DO_NOTHING, db_column='InsuranceNo', primary_key=True)  # Field name made lowercase. The composite primary key (InsuranceNo, ItemCode, ItemCategoryID, VisitTypeID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', related_name='insurancevisittypecustomfee_visittypeid_set')  # Field name made lowercase.
    customfee = models.DecimalField(db_column='CustomFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CurrenciesID', related_name='insurancevisittypecustomfee_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InsuranceVisitTypeCustomFee'
        unique_together = (('insuranceno', 'itemcode', 'itemcategoryid', 'visittypeid'),)


class Insurances(models.Model):
    insuranceid = models.IntegerField(db_column='InsuranceID')  # Field name made lowercase.
    insuranceno = models.CharField(db_column='InsuranceNo', primary_key=True, max_length=20)  # Field name made lowercase.
    insurancename = models.CharField(db_column='InsuranceName', unique=True, max_length=60, blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logophoto = models.BinaryField(db_column='LogoPhoto', blank=True, null=True)  # Field name made lowercase.
    memberdeclaration = models.CharField(db_column='MemberDeclaration', max_length=800, blank=True, null=True)  # Field name made lowercase.
    doctordeclaration = models.CharField(db_column='DoctorDeclaration', max_length=800, blank=True, null=True)  # Field name made lowercase.
    usecustomfee = models.BooleanField(db_column='UseCustomFee', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    accountstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AccountStatusID', blank=True, null=True)  # Field name made lowercase.
    accountbalance = models.DecimalField(db_column='AccountBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    opdoutstanding = models.DecimalField(db_column='OPDOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    extrabilloutstanding = models.DecimalField(db_column='ExtraBillOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastaccountactiondate = models.DateTimeField(db_column='LastAccountActionDate', blank=True, null=True)  # Field name made lowercase.
    tinnumber = models.CharField(db_column='TINNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Insurances'


class Inventory(models.Model):
    tranid = models.AutoField(db_column='TranID', primary_key=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID', related_name='inventory_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    trandate = models.DateTimeField(db_column='TranDate', blank=True, null=True)  # Field name made lowercase.
    stocktypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StockTypeID', related_name='inventory_stocktypeid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    locationunits = models.IntegerField(db_column='LocationUnits', blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    weightedcostaverage = models.DecimalField(db_column='WeightedCostAverage', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BranchID', related_name='inventory_branchid_set', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', related_name='inventory_entrymodeid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    tranreasonid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TranReasonID', related_name='inventory_tranreasonid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventory'


class Inventoryacknowledges(models.Model):
    transferno = models.OneToOneField('Inventorytransferdetailbatches', models.DO_NOTHING, db_column='TransferNo', primary_key=True)  # Field name made lowercase. The composite primary key (TransferNo, ItemCategoryID, ItemCode, BatchNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Inventorytransferdetailbatches', models.DO_NOTHING, db_column='ItemCategoryID', related_name='inventoryacknowledges_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.ForeignKey('Inventorytransferdetailbatches', models.DO_NOTHING, db_column='ItemCode', related_name='inventoryacknowledges_itemcode_set')  # Field name made lowercase.
    receiveddate = models.DateTimeField(db_column='ReceivedDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    batchno = models.ForeignKey('Inventorytransferdetailbatches', models.DO_NOTHING, db_column='BatchNo', related_name='inventoryacknowledges_batchno_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryAcknowledges'
        unique_together = (('transferno', 'itemcategoryid', 'itemcode', 'batchno'),)


class Inventoryext(models.Model):
    tranid = models.OneToOneField(Inventory, models.DO_NOTHING, db_column='TranID', primary_key=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referenceobjectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ReferenceObjectName', blank=True, null=True)  # Field name made lowercase.
    sourceno = models.CharField(db_column='SourceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', related_name='inventoryext_objectname_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryEXT'


class Inventoryint(models.Model):
    tranid = models.IntegerField(db_column='TranID', primary_key=True)  # Field name made lowercase. The composite primary key (TranID, Agent) found, that is not supported. The first column is selected.
    shipstatus = models.BooleanField(db_column='ShipStatus', blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=20)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryINT'
        unique_together = (('tranid', 'agent'),)


class Inventorylocation(models.Model):
    locationid = models.OneToOneField('Lookupdata', models.DO_NOTHING, db_column='LocationID', primary_key=True)  # Field name made lowercase. The composite primary key (LocationID, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID', related_name='inventorylocation_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    unitsathand = models.IntegerField(db_column='UnitsAtHand', blank=True, null=True)  # Field name made lowercase.
    locationorderlevel = models.IntegerField(db_column='LocationOrderLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryLocation'
        unique_together = (('locationid', 'itemcategoryid', 'itemcode'),)


class Inventorylocationbatches(models.Model):
    locationid = models.OneToOneField(Inventorylocation, models.DO_NOTHING, db_column='LocationID', primary_key=True)  # Field name made lowercase. The composite primary key (LocationID, LocationID, ItemCategoryID, ItemCategoryID, ItemCode, BatchNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey(Inventorylocation, models.DO_NOTHING, db_column='ItemCategoryID', related_name='inventorylocationbatches_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.ForeignKey(Inventorylocation, models.DO_NOTHING, db_column='ItemCode', related_name='inventorylocationbatches_itemcode_set')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    batchunitsathand = models.IntegerField(db_column='BatchUnitsAtHand', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryLocationBatches'
        unique_together = (('locationid', 'locationid', 'itemcategoryid', 'itemcategoryid', 'itemcode', 'batchno'),)


class Inventoryorderdetails(models.Model):
    orderno = models.OneToOneField('Inventoryorders', models.DO_NOTHING, db_column='OrderNo', primary_key=True)  # Field name made lowercase. The composite primary key (OrderNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    packid = models.CharField(db_column='PackID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemStatusID', related_name='inventoryorderdetails_itemstatusid_set', blank=True, null=True)  # Field name made lowercase.
    packsize = models.IntegerField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryOrderDetails'
        unique_together = (('orderno', 'itemcategoryid', 'itemcode'),)


class Inventoryorders(models.Model):
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    orderno = models.CharField(db_column='OrderNo', primary_key=True, max_length=20)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    ordertypeid = models.CharField(db_column='OrderTypeID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stockcost = models.DecimalField(db_column='StockCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fromlocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='FromLocationID', blank=True, null=True)  # Field name made lowercase.
    tolocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ToLocationID', related_name='inventoryorders_tolocationid_set', blank=True, null=True)  # Field name made lowercase.
    transferreasonid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TransferReasonID', related_name='inventoryorders_transferreasonid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryOrders'


class Inventorytransferdetailbatches(models.Model):
    transferno = models.OneToOneField('Inventorytransferdetails', models.DO_NOTHING, db_column='TransferNo', primary_key=True)  # Field name made lowercase. The composite primary key (TransferNo, TransferNo, ItemCategoryID, ItemCategoryID, ItemCode, BatchNo) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Inventorytransferdetails', models.DO_NOTHING, db_column='ItemCategoryID', related_name='inventorytransferdetailbatches_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.ForeignKey('Inventorytransferdetails', models.DO_NOTHING, db_column='ItemCode', related_name='inventorytransferdetailbatches_itemcode_set')  # Field name made lowercase.
    stockstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StockStatusID', blank=True, null=True)  # Field name made lowercase.
    packid = models.CharField(db_column='PackID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    packsize = models.IntegerField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    batchquantity = models.IntegerField(db_column='BatchQuantity', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    transferstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='TransferStatusID', related_name='inventorytransferdetailbatches_transferstatusid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransferDetailBatches'
        unique_together = (('transferno', 'transferno', 'itemcategoryid', 'itemcategoryid', 'itemcode', 'batchno'),)


class Inventorytransferdetails(models.Model):
    transferno = models.OneToOneField('Inventorytransfers', models.DO_NOTHING, db_column='TransferNo', primary_key=True)  # Field name made lowercase. The composite primary key (TransferNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransferDetails'
        unique_together = (('transferno', 'itemcategoryid', 'itemcode'),)


class Inventorytransfers(models.Model):
    transferid = models.IntegerField(db_column='TransferID')  # Field name made lowercase.
    transferno = models.CharField(db_column='TransferNo', primary_key=True, max_length=20)  # Field name made lowercase.
    transferdate = models.DateTimeField(db_column='TransferDate', blank=True, null=True)  # Field name made lowercase.
    fromlocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='FromLocationID', blank=True, null=True)  # Field name made lowercase.
    tolocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ToLocationID', related_name='inventorytransfers_tolocationid_set', blank=True, null=True)  # Field name made lowercase.
    orderno = models.ForeignKey(Inventoryorders, models.DO_NOTHING, db_column='OrderNo', blank=True, null=True)  # Field name made lowercase.
    stockcost = models.DecimalField(db_column='StockCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransfers'


class Invoiceadjustments(models.Model):
    adjustmentid = models.IntegerField(db_column='AdjustmentID')  # Field name made lowercase.
    adjustmentno = models.CharField(db_column='AdjustmentNo', primary_key=True, max_length=20)  # Field name made lowercase.
    invoiceno = models.ForeignKey('Invoices', models.DO_NOTHING, db_column='InvoiceNo', blank=True, null=True)  # Field name made lowercase.
    entrylevelid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryLevelID', blank=True, null=True)  # Field name made lowercase.
    adjustmenttypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='AdjustmentTypeID', related_name='invoiceadjustments_adjustmenttypeid_set', blank=True, null=True)  # Field name made lowercase.
    reversalactionid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReversalActionID', related_name='invoiceadjustments_reversalactionid_set', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adjustmentdate = models.DateTimeField(db_column='AdjustmentDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceAdjustments'


class Invoicedetailadjustments(models.Model):
    adjustmentno = models.OneToOneField(Invoiceadjustments, models.DO_NOTHING, db_column='AdjustmentNo', primary_key=True)  # Field name made lowercase. The composite primary key (AdjustmentNo, VisitNo, InvoiceNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey('Invoicedetails', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    invoiceno = models.ForeignKey('Invoicedetails', models.DO_NOTHING, db_column='InvoiceNo', related_name='invoicedetailadjustments_invoiceno_set')  # Field name made lowercase.
    itemcode = models.ForeignKey('Invoicedetails', models.DO_NOTHING, db_column='ItemCode', related_name='invoicedetailadjustments_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Invoicedetails', models.DO_NOTHING, db_column='ItemCategoryID', related_name='invoicedetailadjustments_itemcategoryid_set')  # Field name made lowercase.
    returnreasonid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReturnReasonID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceDetailAdjustments'
        unique_together = (('adjustmentno', 'visitno', 'invoiceno', 'itemcode', 'itemcategoryid'),)


class Invoicedetails(models.Model):
    invoiceno = models.OneToOneField('Invoices', models.DO_NOTHING, db_column='InvoiceNo', primary_key=True)  # Field name made lowercase. The composite primary key (InvoiceNo, VisitNo, ItemCode, ItemCategoryID, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey('Items', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    itemcode = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCode', related_name='invoicedetails_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Items', models.DO_NOTHING, db_column='ItemCategoryID', related_name='invoicedetails_itemcategoryid_set')  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceDetails'
        unique_together = (('invoiceno', 'visitno', 'itemcode', 'itemcategoryid', 'itemcategoryid'),)


class Invoiceextrabillitemadjustments(models.Model):
    adjustmentno = models.OneToOneField(Invoiceadjustments, models.DO_NOTHING, db_column='AdjustmentNo', primary_key=True)  # Field name made lowercase. The composite primary key (AdjustmentNo, ExtraBillNo, InvoiceNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    extrabillno = models.ForeignKey('Invoiceextrabillitems', models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    invoiceno = models.ForeignKey('Invoiceextrabillitems', models.DO_NOTHING, db_column='InvoiceNo', related_name='invoiceextrabillitemadjustments_invoiceno_set')  # Field name made lowercase.
    itemcode = models.ForeignKey('Invoiceextrabillitems', models.DO_NOTHING, db_column='ItemCode', related_name='invoiceextrabillitemadjustments_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Invoiceextrabillitems', models.DO_NOTHING, db_column='ItemCategoryID', related_name='invoiceextrabillitemadjustments_itemcategoryid_set')  # Field name made lowercase.
    returnreasonid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ReturnReasonID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceExtraBillItemAdjustments'
        unique_together = (('adjustmentno', 'extrabillno', 'invoiceno', 'itemcode', 'itemcategoryid'),)


class Invoiceextrabillitems(models.Model):
    invoiceno = models.OneToOneField('Invoices', models.DO_NOTHING, db_column='InvoiceNo', primary_key=True)  # Field name made lowercase. The composite primary key (InvoiceNo, ExtraBillNo, ItemCode, ItemCategoryID, ItemCategoryID) found, that is not supported. The first column is selected.
    extrabillno = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    itemcode = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCode', related_name='invoiceextrabillitems_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='invoiceextrabillitems_itemcategoryid_set')  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InvoiceExtraBillItems'
        unique_together = (('invoiceno', 'extrabillno', 'itemcode', 'itemcategoryid', 'itemcategoryid'),)


class Invoices(models.Model):
    invoiceid = models.IntegerField(db_column='InvoiceID')  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', primary_key=True, max_length=20)  # Field name made lowercase.
    paytypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayTypeID', blank=True, null=True)  # Field name made lowercase.
    payno = models.CharField(db_column='PayNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked', blank=True, null=True)  # Field name made lowercase.
    cancelled = models.BooleanField(db_column='Cancelled', blank=True, null=True)  # Field name made lowercase.
    entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', related_name='invoices_entrymodeid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountpaid = models.DecimalField(db_column='AmountPaid', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invoices'


class Inwardfiles(models.Model):
    outwardno = models.OneToOneField('Outwardfiles', models.DO_NOTHING, db_column='OutwardNo', primary_key=True)  # Field name made lowercase.
    returndatetime = models.DateTimeField(db_column='ReturnDateTime', blank=True, null=True)  # Field name made lowercase.
    returnedby = models.CharField(db_column='ReturnedBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InwardFiles'


class Itemadjustments(models.Model):
    adjustmentno = models.OneToOneField(Billadjustments, models.DO_NOTHING, db_column='AdjustmentNo', primary_key=True)  # Field name made lowercase. The composite primary key (AdjustmentNo, VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    returndate = models.DateTimeField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acknowledgeable = models.BooleanField(db_column='Acknowledgeable', blank=True, null=True)  # Field name made lowercase.
    isacknowledged = models.BooleanField(db_column='IsAcknowledged', blank=True, null=True)  # Field name made lowercase.
    entrylevelid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryLevelID', related_name='itemadjustments_entrylevelid_set', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    invoiceadjustmentno = models.ForeignKey(Invoiceadjustments, models.DO_NOTHING, db_column='InvoiceAdjustmentNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemAdjustments'
        unique_together = (('adjustmentno', 'visitno', 'itemcode', 'itemcategoryid'),)


class Items(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatvalue = models.DecimalField(db_column='VATValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    itemdetails = models.CharField(db_column='ItemDetails', max_length=800, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    itemstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemStatusID', related_name='items_itemstatusid_set', blank=True, null=True)  # Field name made lowercase.
    paystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='PayStatusID', related_name='items_paystatusid_set', blank=True, null=True)  # Field name made lowercase.
    originalquantity = models.IntegerField(db_column='OriginalQuantity', blank=True, null=True)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='OriginalPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    conclusiondate = models.DateTimeField(db_column='ConclusionDate', blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    creatorloginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='CreatorLoginID', related_name='items_creatorloginid_set', blank=True, null=True)  # Field name made lowercase.
    returnquantity = models.IntegerField(db_column='ReturnQuantity', blank=True, null=True)  # Field name made lowercase.
    returnamount = models.DecimalField(db_column='ReturnAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adjustmentcount = models.IntegerField(db_column='AdjustmentCount', blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    referenceno = models.ForeignKey('Paymentrequests', models.DO_NOTHING, db_column='ReferenceNo', blank=True, null=True)  # Field name made lowercase.
    isverified = models.BooleanField(db_column='IsVerified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Items'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'), ('visitno', 'itemcategoryid', 'itemcode'),)


class Itemsbalancedetails(models.Model):
    visitno = models.OneToOneField(Items, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='itemsbalancedetails_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='itemsbalancedetails_itemcategoryid_set')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800, blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    balancestatus = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='BalanceStatus', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    nextvisitno = models.CharField(db_column='NextVisitNo', max_length=20)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemsBalanceDetails'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Itemscash(models.Model):
    visitno = models.OneToOneField(Items, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='itemscash_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='itemscash_itemcategoryid_set')  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cashamount = models.DecimalField(db_column='CashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cashpaystatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='CashPayStatusID', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemsCASH'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Itemscomplement(models.Model):
    itemscomplementid = models.AutoField(db_column='ItemsComplementID', primary_key=True)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    treatmentno = models.CharField(db_column='TreatmentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='itemCategoryID', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    complementitemcode = models.CharField(db_column='ComplementItemCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    complementitemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ComplementItemCategoryID', related_name='itemscomplement_complementitemcategoryid_set', blank=True, null=True)  # Field name made lowercase.
    complementitemname = models.CharField(db_column='ComplementItemName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    itemstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemStatusID', related_name='itemscomplement_itemstatusid_set', blank=True, null=True)  # Field name made lowercase.
    visittypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='VisitTypeID', related_name='itemscomplement_visittypeid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    sourceobjectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='SourceObjectName', related_name='itemscomplement_sourceobjectname_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemsComplement'
        unique_together = (('objectname', 'sourceobjectname', 'treatmentno', 'itemcode', 'itemcategoryid', 'complementitemcode', 'complementitemcategoryid'),)


class Itemsext(models.Model):
    visitno = models.OneToOneField(Items, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='itemsext_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='itemsext_itemcategoryid_set')  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    drquantity = models.IntegerField(db_column='DrQuantity', blank=True, null=True)  # Field name made lowercase.
    issuedatetime = models.DateTimeField(db_column='IssueDateTime', blank=True, null=True)  # Field name made lowercase.
    pharmacist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Pharmacist', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemsEXT'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Itemsincome(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    copayamount = models.DecimalField(db_column='CopayAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    vatvalue = models.DecimalField(db_column='VATValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemsIncome'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Labpossibleresults(models.Model):
    testcode = models.OneToOneField('Labtests', models.DO_NOTHING, db_column='TestCode', primary_key=True)  # Field name made lowercase. The composite primary key (TestCode, PossibleResult) found, that is not supported. The first column is selected.
    possibleresult = models.CharField(db_column='PossibleResult', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabPossibleResults'
        unique_together = (('testcode', 'possibleresult'),)


class Labrequestdetails(models.Model):
    specimenno = models.OneToOneField('Labrequests', models.DO_NOTHING, db_column='SpecimenNo', primary_key=True)  # Field name made lowercase. The composite primary key (SpecimenNo, TestCode) found, that is not supported. The first column is selected.
    testcode = models.ForeignKey('Labtests', models.DO_NOTHING, db_column='TestCode')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=800, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    specimentypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SpecimenTypeID', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    samplequalityid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SampleQualityID', related_name='labrequestdetails_samplequalityid_set', blank=True, null=True)  # Field name made lowercase.
    samplesuitabilityid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SampleSuitabilityID', related_name='labrequestdetails_samplesuitabilityid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabRequestDetails'
        unique_together = (('specimenno', 'testcode'),)


class Labrequests(models.Model):
    specimenid = models.IntegerField(db_column='SpecimenID')  # Field name made lowercase.
    specimenno = models.CharField(db_column='SpecimenNo', primary_key=True, max_length=20)  # Field name made lowercase.
    drawnby = models.ForeignKey('Staff', models.DO_NOTHING, db_column='DrawnBy', blank=True, null=True)  # Field name made lowercase.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    drawndatetime = models.DateTimeField(db_column='DrawnDateTime', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    collectiondatetime = models.DateTimeField(db_column='CollectionDateTime', blank=True, null=True)  # Field name made lowercase.
    lablocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LabLocationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabRequests'


class Labrequestsipd(models.Model):
    specimenno = models.OneToOneField(Labrequests, models.DO_NOTHING, db_column='SpecimenNo', primary_key=True)  # Field name made lowercase.
    roundno = models.ForeignKey(Ipddoctor, models.DO_NOTHING, db_column='RoundNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabRequestsIPD'


class Labresultapprovals(models.Model):
    specimenno = models.OneToOneField('Labresults', models.DO_NOTHING, db_column='SpecimenNo', primary_key=True)  # Field name made lowercase. The composite primary key (SpecimenNo, TestCode) found, that is not supported. The first column is selected.
    testcode = models.ForeignKey('Labresults', models.DO_NOTHING, db_column='TestCode', related_name='labresultapprovals_testcode_set')  # Field name made lowercase.
    testname = models.CharField(db_column='TestName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    approvaldatetime = models.DateTimeField(db_column='ApprovalDateTime', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.ForeignKey('Staff', models.DO_NOTHING, db_column='ApprovedBy', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabResultApprovals'
        unique_together = (('specimenno', 'testcode'),)


class Labresultcrosschecks(models.Model):
    specimenno = models.OneToOneField('Labresults', models.DO_NOTHING, db_column='SpecimenNo', primary_key=True)  # Field name made lowercase. The composite primary key (SpecimenNo, TestCode) found, that is not supported. The first column is selected.
    testcode = models.ForeignKey('Labresults', models.DO_NOTHING, db_column='TestCode', related_name='labresultcrosschecks_testcode_set')  # Field name made lowercase.
    crosscheckeddatetime = models.DateTimeField(db_column='CrossCheckedDateTime', blank=True, null=True)  # Field name made lowercase.
    crosscheckedby = models.ForeignKey('Staff', models.DO_NOTHING, db_column='CrossCheckedBy')  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabResultCrossChecks'
        unique_together = (('specimenno', 'testcode'),)


class Labresults(models.Model):
    specimenno = models.OneToOneField(Labrequestdetails, models.DO_NOTHING, db_column='SpecimenNo', primary_key=True)  # Field name made lowercase. The composite primary key (SpecimenNo, TestCode) found, that is not supported. The first column is selected.
    testcode = models.ForeignKey(Labrequestdetails, models.DO_NOTHING, db_column='TestCode', related_name='labresults_testcode_set')  # Field name made lowercase.
    testdatetime = models.DateTimeField(db_column='TestDateTime', blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    normalrange = models.CharField(db_column='NormalRange', max_length=800, blank=True, null=True)  # Field name made lowercase.
    resultflagid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultFlagID', blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    labtechnologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='LabTechnologist', blank=True, null=True)  # Field name made lowercase.
    entrymodeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='EntryModeID', related_name='labresults_entrymodeid_set', blank=True, null=True)  # Field name made lowercase.
    approvedstatusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ApprovedStatusID', related_name='labresults_approvedstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    testinstrumentno = models.ForeignKey('Testinstruments', models.DO_NOTHING, db_column='TestInstrumentNo', blank=True, null=True)  # Field name made lowercase.
    lablocationid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LabLocationID', related_name='labresults_lablocationid_set', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    crosschecked = models.BooleanField(db_column='CrossChecked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabResults'
        unique_together = (('specimenno', 'testcode'),)


class Labresultsext(models.Model):
    specimenno = models.OneToOneField(Labresults, models.DO_NOTHING, db_column='SpecimenNo', primary_key=True)  # Field name made lowercase. The composite primary key (SpecimenNo, TestCode, TestCode, SubTestCode) found, that is not supported. The first column is selected.
    testcode = models.ForeignKey('Labtestsext', models.DO_NOTHING, db_column='TestCode')  # Field name made lowercase.
    subtestcode = models.ForeignKey('Labtestsext', models.DO_NOTHING, db_column='SubTestCode', related_name='labresultsext_subtestcode_set')  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    normalrange = models.CharField(db_column='NormalRange', max_length=800, blank=True, null=True)  # Field name made lowercase.
    resultflagid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultFlagID', blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabResultsEXT'
        unique_together = (('specimenno', 'testcode', 'testcode', 'subtestcode'),)


class Labtestmeasurementprocedures(models.Model):
    testcode = models.OneToOneField('Labtests', models.DO_NOTHING, db_column='TestCode', primary_key=True)  # Field name made lowercase. The composite primary key (TestCode, MeasurementProcedureID) found, that is not supported. The first column is selected.
    measurementprocedureid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='MeasurementProcedureID')  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabTestMeasurementProcedures'
        unique_together = (('testcode', 'measurementprocedureid'),)


class Labtests(models.Model):
    testid = models.IntegerField(db_column='TestID')  # Field name made lowercase.
    testcode = models.CharField(db_column='TestCode', primary_key=True, max_length=20)  # Field name made lowercase.
    testname = models.CharField(db_column='TestName', unique=True, max_length=100)  # Field name made lowercase.
    specimentypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='SpecimenTypeID', blank=True, null=True)  # Field name made lowercase.
    labsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LabsID', related_name='labtests_labsid_set', blank=True, null=True)  # Field name made lowercase.
    normalrange = models.TextField(db_column='NormalRange', blank=True, null=True)  # Field name made lowercase.
    unitmeasureid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='UnitMeasureID', related_name='labtests_unitmeasureid_set', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    testfee = models.DecimalField(db_column='TestFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    resultdatatypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultDataTypeID', related_name='labtests_resultdatatypeid_set', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    requiresresultsapproval = models.BooleanField(db_column='RequiresResultsApproval', blank=True, null=True)  # Field name made lowercase.
    tubetype = models.CharField(db_column='TubeType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    testdescription = models.CharField(db_column='TestDescription', max_length=500, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabTests'


class Labtestsext(models.Model):
    sortorder = models.SmallIntegerField(db_column='SortOrder', blank=True, null=True)  # Field name made lowercase.
    testcode = models.OneToOneField(Labtests, models.DO_NOTHING, db_column='TestCode', primary_key=True)  # Field name made lowercase. The composite primary key (TestCode, SubTestCode) found, that is not supported. The first column is selected.
    subtestcode = models.CharField(db_column='SubTestCode', max_length=20)  # Field name made lowercase.
    subtestname = models.CharField(db_column='SubTestName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    normalrange = models.TextField(db_column='NormalRange', blank=True, null=True)  # Field name made lowercase.
    unitmeasureid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='UnitMeasureID', blank=True, null=True)  # Field name made lowercase.
    resultdatatypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='ResultDataTypeID', related_name='labtestsext_resultdatatypeid_set', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabTestsEXT'
        unique_together = (('testcode', 'subtestcode'), ('testcode', 'subtestname'),)


class Labtestsextpossibleresults(models.Model):
    testcode = models.OneToOneField(Labtests, models.DO_NOTHING, db_column='TestCode', primary_key=True)  # Field name made lowercase. The composite primary key (TestCode, SubTestCode, PossibleResults) found, that is not supported. The first column is selected.
    subtestcode = models.CharField(db_column='SubTestCode', max_length=20)  # Field name made lowercase.
    possibleresults = models.CharField(db_column='PossibleResults', max_length=200)  # Field name made lowercase.
    loginid = models.ForeignKey('Logins', models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabTestsEXTPossibleResults'
        unique_together = (('testcode', 'subtestcode', 'possibleresults'),)


class Licenses(models.Model):
    lln = models.CharField(db_column='LLN', primary_key=True, max_length=100)  # Field name made lowercase.
    lco = models.CharField(db_column='LCO', max_length=100)  # Field name made lowercase.
    lsp = models.CharField(db_column='LSP', max_length=100)  # Field name made lowercase.
    lse = models.CharField(db_column='LSE', max_length=100)  # Field name made lowercase.
    lsw = models.CharField(db_column='LSW', max_length=100)  # Field name made lowercase.
    lci = models.CharField(db_column='LCI', max_length=100)  # Field name made lowercase.
    lpo = models.CharField(db_column='LPO', max_length=100)  # Field name made lowercase.
    lcd = models.CharField(db_column='LCD', max_length=100)  # Field name made lowercase.
    lsd = models.CharField(db_column='LSD', max_length=100)  # Field name made lowercase.
    led = models.CharField(db_column='LED', max_length=100)  # Field name made lowercase.
    lwd = models.CharField(db_column='LWD', max_length=100)  # Field name made lowercase.
    lnu = models.CharField(db_column='LNU', max_length=100)  # Field name made lowercase.
    lid = models.CharField(db_column='LID', max_length=100)  # Field name made lowercase.
    lkt = models.CharField(db_column='LKT', max_length=100)  # Field name made lowercase.
    lnr = models.CharField(db_column='LNR', max_length=100)  # Field name made lowercase.
    lwr = models.CharField(db_column='LWR', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Licenses'


class Locations(models.Model):
    locationid = models.OneToOneField('Lookupdata', models.DO_NOTHING, db_column='LocationID', primary_key=True)  # Field name made lowercase.
    locationtypeid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='LocationTypeID', related_name='locations_locationtypeid_set', blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Locations'


class Logger(models.Model):
    loggerid = models.AutoField(db_column='LoggerID', primary_key=True)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    objectkey = models.CharField(db_column='ObjectKey', max_length=200, blank=True, null=True)  # Field name made lowercase.
    logaction = models.CharField(db_column='LogAction', max_length=1, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logger'


class Loginroles(models.Model):
    loginid = models.OneToOneField('Logins', models.DO_NOTHING, db_column='LoginID', primary_key=True)  # Field name made lowercase. The composite primary key (LoginID, RoleName) found, that is not supported. The first column is selected.
    rolename = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RoleName')  # Field name made lowercase.
    assigndate = models.DateTimeField(db_column='AssignDate', blank=True, null=True)  # Field name made lowercase.
    roleexpires = models.BooleanField(db_column='RoleExpires', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoginRoles'
        unique_together = (('loginid', 'rolename'),)


class Logins(models.Model):
    loginid = models.CharField(db_column='LoginID', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
    loginpassword = models.CharField(db_column='LoginPassword', max_length=200)  # Field name made lowercase.
    loginlevel = models.SmallIntegerField(db_column='LoginLevel')  # Field name made lowercase.
    statusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StatusID')  # Field name made lowercase.
    changepassword = models.BooleanField(db_column='ChangePassword')  # Field name made lowercase.
    creatorloginid = models.ForeignKey('self', models.DO_NOTHING, db_column='CreatorLoginID', blank=True, null=True)  # Field name made lowercase.
    creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    creatorrecorddatetime = models.DateTimeField(db_column='CreatorRecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logins'


class Lookupdata(models.Model):
    lookuporder = models.AutoField(primary_key=True, db_column='LookupOrder')  # Field name made lowercase.
    dataid = models.CharField(db_column='DataID', max_length=10)  # Field name made lowercase.
    objectid = models.ForeignKey('Lookupobjects', models.DO_NOTHING, db_column='ObjectID')  # Field name made lowercase.
    datades = models.CharField(db_column='DataDes', max_length=100)  # Field name made lowercase.
    isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
    ishidden = models.CharField(db_column='IsHidden', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookupData'
        unique_together = (('objectid', 'datades'),)


class Lookupdatamappings(models.Model):
    dataid = models.OneToOneField(Lookupdata, models.DO_NOTHING, db_column='DataID', primary_key=True)  # Field name made lowercase. The composite primary key (DataID, AgentNo) found, that is not supported. The first column is selected.
    agentno = models.ForeignKey(Intagents, models.DO_NOTHING, db_column='AgentNo')  # Field name made lowercase.
    agentdataid = models.CharField(db_column='AgentDataID', max_length=10)  # Field name made lowercase.
    objectname = models.CharField(db_column='ObjectName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookupDataMappings'
        unique_together = (('dataid', 'agentno'),)


class Lookupobjects(models.Model):
    objectid = models.SmallIntegerField(db_column='ObjectID', primary_key=True)  # Field name made lowercase.
    objectname = models.CharField(db_column='ObjectName', unique=True, max_length=40)  # Field name made lowercase.
    objectdes = models.CharField(db_column='ObjectDes', unique=True, max_length=60)  # Field name made lowercase.
    isreadonly = models.CharField(db_column='IsReadOnly', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookupObjects'


class Lowvision(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    briefhistory = models.CharField(db_column='BriefHistory', max_length=200, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=200, blank=True, null=True)  # Field name made lowercase.
    majoroculardiagnosisre = models.CharField(db_column='MajorOcularDiagnosisRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    majoroculardiagnosisle = models.CharField(db_column='MajorOcularDiagnosisLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    otheroculardiagnosisre = models.CharField(db_column='OtherOcularDiagnosisRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    otheroculardiagnosisle = models.CharField(db_column='OtherOcularDiagnosisLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ophthalmologistseenid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='OphthalmologistSeenID', blank=True, null=True)  # Field name made lowercase.
    otherimpairmentsid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='OtherImpairmentsID', related_name='lowvision_otherimpairmentsid_set', blank=True, null=True)  # Field name made lowercase.
    otherimpairments = models.CharField(db_column='OtherImpairments', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingtreatmentfarre = models.CharField(db_column='ExistingTreatmentFarRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingtreatmentfarle = models.CharField(db_column='ExistingTreatmentFarLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingtreatmentnearre = models.CharField(db_column='ExistingTreatmentNearRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingtreatmentnearle = models.CharField(db_column='ExistingTreatmentNearLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newtreatmentfarre = models.CharField(db_column='NewTreatmentFarRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newtreatmentfarle = models.CharField(db_column='NewTreatmentFarLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newtreatmentnearre = models.CharField(db_column='NewTreatmentNearRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newtreatmentnearle = models.CharField(db_column='NewTreatmentNearLE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingvisualacuityfarleid = models.CharField(db_column='ExistingVisualAcuityFarLEID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingvisualacuityfarreid = models.CharField(db_column='ExistingVisualAcuityFarREID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingvisualacuitynearleid = models.CharField(db_column='ExistingVisualAcuityNearLEID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existingvisualacuitynearreid = models.CharField(db_column='ExistingVisualAcuityNearREID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newvisualacuityfarleid = models.CharField(db_column='NewVisualAcuityFarLEID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newvisualacuityfarreid = models.CharField(db_column='NewVisualAcuityFarREID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newvisualacuitynearleid = models.CharField(db_column='NewVisualAcuityNearLEID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    newvisualacuitynearreid = models.CharField(db_column='NewVisualAcuityNearREID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existinglvdsnear = models.CharField(db_column='ExistingLVDsNear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    existinglvdsfar = models.CharField(db_column='ExistingLVDsFar', max_length=200, blank=True, null=True)  # Field name made lowercase.
    problemencounteredlvdsnear = models.CharField(db_column='ProblemEncounteredLVDsNear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    problemencounteredlvdsfar = models.CharField(db_column='ProblemEncounteredLVDsFar', max_length=200, blank=True, null=True)  # Field name made lowercase.
    colourvisiondefectid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ColourVisionDefectID', related_name='lowvision_colourvisiondefectid_set', blank=True, null=True)  # Field name made lowercase.
    colourvisiontestused = models.CharField(db_column='ColourVisionTestUsed', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contrastsensitivityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ContrastSensitivityID', related_name='lowvision_contrastsensitivityid_set', blank=True, null=True)  # Field name made lowercase.
    contrastsensitivitytestused = models.CharField(db_column='ContrastSensitivityTestUsed', max_length=200, blank=True, null=True)  # Field name made lowercase.
    visualfielddefectid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisualFieldDefectID', related_name='lowvision_visualfielddefectid_set', blank=True, null=True)  # Field name made lowercase.
    visualfielddefecttestused = models.CharField(db_column='VisualFieldDefectTestUsed', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lowvisiondevicesfar = models.CharField(db_column='LowVisionDevicesFar', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lowvisiondevicesnear = models.CharField(db_column='LowVisionDevicesNear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nonopticalaids = models.CharField(db_column='NonOpticalAids', max_length=200, blank=True, null=True)  # Field name made lowercase.
    advice = models.CharField(db_column='Advice', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LowVision'


class Mappedcodes(models.Model):
    accountno = models.OneToOneField(Billcustomers, models.DO_NOTHING, db_column='AccountNo', primary_key=True)  # Field name made lowercase. The composite primary key (AccountNo, ItemCode, ItemCategoryID, LoginID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=200)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    customcode = models.CharField(db_column='CustomCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MappedCodes'
        unique_together = (('accountno', 'itemcode', 'itemcategoryid', 'loginid'),)


class Mappedcodesfinance(models.Model):
    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (ItemCode, ItemCategoryID, AccountTypeID) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    accounttypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AccountTypeID', related_name='mappedcodesfinance_accounttypeid_set')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MappedCodesFinance'
        unique_together = (('itemcode', 'itemcategoryid', 'accounttypeid'),)


class Maternityservices(models.Model):
    maternityid = models.IntegerField(db_column='MaternityID')  # Field name made lowercase.
    maternitycode = models.CharField(db_column='MaternityCode', primary_key=True, max_length=20)  # Field name made lowercase.
    maternityname = models.CharField(db_column='MaternityName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaternityServices'


class Memberbenefits(models.Model):
    benefitcode = models.CharField(db_column='BenefitCode', primary_key=True, max_length=20)  # Field name made lowercase.
    benefitname = models.CharField(db_column='BenefitName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberBenefits'


class Memberlimits(models.Model):
    medicalcardno = models.OneToOneField(Billcustomermembers, models.DO_NOTHING, db_column='MedicalCardNo', primary_key=True)  # Field name made lowercase. The composite primary key (MedicalCardNo, AccountNo, BenefitCode) found, that is not supported. The first column is selected.
    accountno = models.ForeignKey(Billcustomermembers, models.DO_NOTHING, db_column='AccountNo', related_name='memberlimits_accountno_set')  # Field name made lowercase.
    benefitcode = models.ForeignKey(Memberbenefits, models.DO_NOTHING, db_column='BenefitCode')  # Field name made lowercase.
    memberlimit = models.DecimalField(db_column='MemberLimit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MemberLimits'
        unique_together = (('medicalcardno', 'accountno', 'benefitcode'),)


class Messenger(models.Model):
    receiverstaffno = models.ForeignKey(Logins, models.DO_NOTHING, db_column='ReceiverStaffNo', blank=True, null=True)  # Field name made lowercase.
    messageinfo = models.TextField(db_column='MessageInfo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', related_name='messenger_loginid_set', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Messenger'


class Opddiagnosisarchive(models.Model):
    visitno = models.CharField(db_column='VisitNo', max_length=20)  # Field name made lowercase.
    diseasecode = models.CharField(db_column='DiseaseCode', max_length=10)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPDDiagnosisArchive'


class Opdstaffpaymentdetails(models.Model):
    paymentvoucherno = models.OneToOneField('Staffpayments', models.DO_NOTHING, db_column='PaymentVoucherNo', primary_key=True)  # Field name made lowercase. The composite primary key (PaymentVoucherNo, VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey(Items, models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='opdstaffpaymentdetails_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='opdstaffpaymentdetails_itemcategoryid_set')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    approvalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ApprovalStatusID')  # Field name made lowercase.
    approvalnotes = models.CharField(db_column='ApprovalNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPDStaffPaymentDetails'
        unique_together = (('paymentvoucherno', 'visitno', 'itemcode', 'itemcategoryid'),)


class Otintervention(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    leadtherapist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='LeadTherapist', blank=True, null=True)  # Field name made lowercase.
    interventiontypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='InterventionTypeID', blank=True, null=True)  # Field name made lowercase.
    cognitiveassessment = models.BooleanField(db_column='CognitiveAssessment', blank=True, null=True)  # Field name made lowercase.
    handtherapy = models.BooleanField(db_column='HandTherapy', blank=True, null=True)  # Field name made lowercase.
    healtheducation = models.BooleanField(db_column='HealthEducation', blank=True, null=True)  # Field name made lowercase.
    therapeuticgroupactivities = models.BooleanField(db_column='TherapeuticGroupActivities', blank=True, null=True)  # Field name made lowercase.
    homebasedrehabilitation = models.BooleanField(db_column='HomebasedRehabilitation', blank=True, null=True)  # Field name made lowercase.
    assistivedevices = models.BooleanField(db_column='AssistiveDevices', blank=True, null=True)  # Field name made lowercase.
    mobilityskillstraining = models.BooleanField(db_column='MobilitySkillsTraining', blank=True, null=True)  # Field name made lowercase.
    neurocognitiverehabilitation = models.BooleanField(db_column='NeurocognitiveRehabilitation', blank=True, null=True)  # Field name made lowercase.
    orientationtechniques = models.BooleanField(db_column='OrientationTechniques', blank=True, null=True)  # Field name made lowercase.
    vocationalrehabilitation = models.BooleanField(db_column='VocationalRehabilitation', blank=True, null=True)  # Field name made lowercase.
    selfcaretraining = models.BooleanField(db_column='SelfCareTraining', blank=True, null=True)  # Field name made lowercase.
    playtherapy = models.BooleanField(db_column='PlayTherapy', blank=True, null=True)  # Field name made lowercase.
    stressmanagement = models.BooleanField(db_column='StressManagement', blank=True, null=True)  # Field name made lowercase.
    otherassessment = models.CharField(db_column='OtherAssessment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTIntervention'


class Objectroles(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName', primary_key=True)  # Field name made lowercase. The composite primary key (ObjectName, RoleName) found, that is not supported. The first column is selected.
    rolename = models.ForeignKey('Roles', models.DO_NOTHING, db_column='RoleName')  # Field name made lowercase.
    write = models.BooleanField(db_column='Write', blank=True, null=True)  # Field name made lowercase.
    read = models.BooleanField(db_column='Read', blank=True, null=True)  # Field name made lowercase.
    update = models.BooleanField(db_column='Update', blank=True, null=True)  # Field name made lowercase.
    delete = models.BooleanField(db_column='Delete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObjectRoles'
        unique_together = (('objectname', 'rolename'),)


class Obstetric(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, Pregnancy) found, that is not supported. The first column is selected.
    pregnancy = models.IntegerField(db_column='Pregnancy', unique=True)  # Field name made lowercase.
    yearpregnant = models.IntegerField(db_column='YearPregnant', blank=True, null=True)  # Field name made lowercase.
    abortionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AbortionID', blank=True, null=True)  # Field name made lowercase.
    abortionperiodid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AbortionPeriodID', related_name='obstetric_abortionperiodid_set', blank=True, null=True)  # Field name made lowercase.
    typeofdeliveryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TypeOfDeliveryID', related_name='obstetric_typeofdeliveryid_set', blank=True, null=True)  # Field name made lowercase.
    thirdstageid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ThirdStageID', related_name='obstetric_thirdstageid_set', blank=True, null=True)  # Field name made lowercase.
    puerperiumid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PuerPeriumID', related_name='obstetric_puerperiumid_set', blank=True, null=True)  # Field name made lowercase.
    childstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ChildStatusID', related_name='obstetric_childstatusid_set', blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GenderID', related_name='obstetric_genderid_set', blank=True, null=True)  # Field name made lowercase.
    birthweight = models.DecimalField(db_column='BirthWeight', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    childimmunised = models.BooleanField(db_column='ChildImmunised', blank=True, null=True)  # Field name made lowercase.
    healthcondition = models.CharField(db_column='HealthCondition', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Obstetric'
        unique_together = (('patientno', 'pregnancy'),)


class Obstetrichistory(models.Model):
    patientno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    gravidity = models.IntegerField(db_column='Gravidity', blank=True, null=True)  # Field name made lowercase.
    parity = models.IntegerField(db_column='Parity', blank=True, null=True)  # Field name made lowercase.
    noofsurvivingchildren = models.IntegerField(db_column='NoOfSurvivingChildren', blank=True, null=True)  # Field name made lowercase.
    lmp = models.DateTimeField(db_column='LMP', blank=True, null=True)  # Field name made lowercase.
    edd = models.DateTimeField(db_column='EDD', blank=True, null=True)  # Field name made lowercase.
    gestationalageinwks = models.IntegerField(db_column='GestationalAgeInWks', blank=True, null=True)  # Field name made lowercase.
    stillbirth = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StillBirth', blank=True, null=True)  # Field name made lowercase.
    noofstillbirths = models.IntegerField(db_column='NoOfStillBirths', blank=True, null=True)  # Field name made lowercase.
    abortions = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Abortions', related_name='obstetrichistory_abortions_set', blank=True, null=True)  # Field name made lowercase.
    noofabortions = models.IntegerField(db_column='NoOfAbortions', blank=True, null=True)  # Field name made lowercase.
    caesarian = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Caesarian', related_name='obstetrichistory_caesarian_set', blank=True, null=True)  # Field name made lowercase.
    noofcaesarians = models.IntegerField(db_column='NoOfCaesarians', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObstetricHistory'


class Occupationaltherapy(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    walkingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='WalkingID', blank=True, null=True)  # Field name made lowercase.
    sitstandtransfersid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SitStandTransfersID', related_name='occupationaltherapy_sitstandtransfersid_set', blank=True, null=True)  # Field name made lowercase.
    bathingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BathingID', related_name='occupationaltherapy_bathingid_set', blank=True, null=True)  # Field name made lowercase.
    toiletingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ToiletingID', related_name='occupationaltherapy_toiletingid_set', blank=True, null=True)  # Field name made lowercase.
    dressingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DressingID', related_name='occupationaltherapy_dressingid_set', blank=True, null=True)  # Field name made lowercase.
    handfunctionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='HandFunctionID', related_name='occupationaltherapy_handfunctionid_set', blank=True, null=True)  # Field name made lowercase.
    washingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='WashingID', related_name='occupationaltherapy_washingid_set', blank=True, null=True)  # Field name made lowercase.
    feedingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='FeedingID', related_name='occupationaltherapy_feedingid_set', blank=True, null=True)  # Field name made lowercase.
    groomingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GroomingID', related_name='occupationaltherapy_groomingid_set', blank=True, null=True)  # Field name made lowercase.
    mealpreparationid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MealPreparationID', related_name='occupationaltherapy_mealpreparationid_set', blank=True, null=True)  # Field name made lowercase.
    workplayschoolid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='WorkPlaySchoolID', related_name='occupationaltherapy_workplayschoolid_set', blank=True, null=True)  # Field name made lowercase.
    leisureid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='LeisureID', related_name='occupationaltherapy_leisureid_set', blank=True, null=True)  # Field name made lowercase.
    communicationid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CommunicationID', related_name='occupationaltherapy_communicationid_set', blank=True, null=True)  # Field name made lowercase.
    cognitionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CognitionID', related_name='occupationaltherapy_cognitionid_set', blank=True, null=True)  # Field name made lowercase.
    attentionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AttentionID', related_name='occupationaltherapy_attentionid_set', blank=True, null=True)  # Field name made lowercase.
    impulsecontrolid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ImpulseControlID', related_name='occupationaltherapy_impulsecontrolid_set', blank=True, null=True)  # Field name made lowercase.
    sleepid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SleepID', related_name='occupationaltherapy_sleepid_set', blank=True, null=True)  # Field name made lowercase.
    memoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MemoryID', related_name='occupationaltherapy_memoryid_set', blank=True, null=True)  # Field name made lowercase.
    perceptionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PerceptionID', related_name='occupationaltherapy_perceptionid_set', blank=True, null=True)  # Field name made lowercase.
    thoughtid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ThoughtID', related_name='occupationaltherapy_thoughtid_set', blank=True, null=True)  # Field name made lowercase.
    sightid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SightID', related_name='occupationaltherapy_sightid_set', blank=True, null=True)  # Field name made lowercase.
    tasteid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TasteID', related_name='occupationaltherapy_tasteid_set', blank=True, null=True)  # Field name made lowercase.
    hearingid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='HearingID', related_name='occupationaltherapy_hearingid_set', blank=True, null=True)  # Field name made lowercase.
    touchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TouchID', related_name='occupationaltherapy_touchid_set', blank=True, null=True)  # Field name made lowercase.
    smellid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SmellID', related_name='occupationaltherapy_smellid_set', blank=True, null=True)  # Field name made lowercase.
    painid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PainID', related_name='occupationaltherapy_painid_set', blank=True, null=True)  # Field name made lowercase.
    vestibularid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VestibularID', related_name='occupationaltherapy_vestibularid_set', blank=True, null=True)  # Field name made lowercase.
    temperatureandpressureid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TemperatureAndPressureID', related_name='occupationaltherapy_temperatureandpressureid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OccupationalTherapy'


class Oldlabrequests(models.Model):
    specimenid = models.IntegerField(db_column='SpecimenID', blank=True, null=True)  # Field name made lowercase.
    specimenno = models.CharField(db_column='SpecimenNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specimendes = models.CharField(db_column='SpecimenDes', max_length=40, blank=True, null=True)  # Field name made lowercase.
    drawnby = models.CharField(db_column='DrawnBy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    visitno = models.CharField(db_column='VisitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drawndatetime = models.DateTimeField(db_column='DrawnDateTime', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OldLabRequests'


class Optical(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    rightsph = models.CharField(db_column='RightSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightcyl = models.CharField(db_column='RightCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightaxis = models.CharField(db_column='RightAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightprism = models.CharField(db_column='RightPRISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightadd = models.CharField(db_column='RightADD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftsph = models.CharField(db_column='LeftSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftcyl = models.CharField(db_column='LeftCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftaxis = models.CharField(db_column='LeftAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftprism = models.CharField(db_column='LeftPRISM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftadd = models.CharField(db_column='LeftADD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lensetypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='LenseTypeID', blank=True, null=True)  # Field name made lowercase.
    pd = models.SmallIntegerField(db_column='Pd', blank=True, null=True)  # Field name made lowercase.
    sg = models.SmallIntegerField(db_column='Sg', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Optical'


class Opticalservices(models.Model):
    opticalid = models.IntegerField(db_column='OpticalID')  # Field name made lowercase.
    opticalcode = models.CharField(db_column='OpticalCode', primary_key=True, max_length=20)  # Field name made lowercase.
    opticalname = models.CharField(db_column='OpticalName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    opticalcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='OpticalCategoryID', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unitmeasureid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='UnitMeasureID', related_name='opticalservices_unitmeasureid_set', blank=True, null=True)  # Field name made lowercase.
    locationid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='LocationID', related_name='opticalservices_locationid_set', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OpticalServices'


class Options(models.Model):
    optionname = models.CharField(db_column='OptionName', primary_key=True, max_length=100)  # Field name made lowercase.
    optionvalue = models.CharField(db_column='OptionValue', max_length=200)  # Field name made lowercase.
    datatypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DataTypeID')  # Field name made lowercase.
    maxlength = models.SmallIntegerField(db_column='MaxLength')  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Options'


class Orthoptics(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    headposture = models.CharField(db_column='HeadPosture', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fixation = models.CharField(db_column='Fixation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lefthirschberg = models.CharField(db_column='LeftHirschberg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    righthirschberg = models.CharField(db_column='RightHirschberg', max_length=200, blank=True, null=True)  # Field name made lowercase.
    righteom = models.CharField(db_column='RightEOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lefteom = models.CharField(db_column='LeftEOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    covertestid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CoverTestID', blank=True, null=True)  # Field name made lowercase.
    leftapctglasses = models.CharField(db_column='LeftAPCTGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightapctglasses = models.CharField(db_column='RightAPCTGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftapctwithoutglasses = models.CharField(db_column='LeftAPCTWithOutGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightapctwithoutglasses = models.CharField(db_column='RightAPCTWithOutGlasses', max_length=200, blank=True, null=True)  # Field name made lowercase.
    correspondence = models.CharField(db_column='Correspondence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prismadaptation = models.CharField(db_column='PrismAdaptation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fusionconvergence = models.CharField(db_column='FusionConvergence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fusiondivergence = models.CharField(db_column='FusionDivergence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fusionrange = models.CharField(db_column='FusionRange', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nearpointofaccommodation = models.CharField(db_column='NearPointOfAccommodation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nearpointofconvergence = models.CharField(db_column='NearPointOfConvergence', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orthopticsnotes = models.CharField(db_column='OrthopticsNotes', max_length=400, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    stereopsis = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Stereopsis', related_name='orthoptics_stereopsis_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orthoptics'


class Otherincome(models.Model):
    incomeid = models.IntegerField(db_column='IncomeID')  # Field name made lowercase.
    incomeno = models.CharField(db_column='IncomeNo', primary_key=True, max_length=20)  # Field name made lowercase.
    incomedate = models.DateTimeField(db_column='IncomeDate', blank=True, null=True)  # Field name made lowercase.
    incomesourcesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='IncomeSourcesID', blank=True, null=True)  # Field name made lowercase.
    paymodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayModesID', related_name='otherincome_paymodesid_set', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', related_name='otherincome_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    amounttendered = models.DecimalField(db_column='AmountTendered', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', related_name='otherincome_branchid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherIncome'


class Otheritems(models.Model):
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', primary_key=True, max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    groupsid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GroupsID', related_name='otheritems_groupsid_set', blank=True, null=True)  # Field name made lowercase.
    unitmeasureid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='UnitMeasureID', related_name='otheritems_unitmeasureid_set', blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    orderlevel = models.IntegerField(db_column='OrderLevel', blank=True, null=True)  # Field name made lowercase.
    keepingunit = models.IntegerField(db_column='KeepingUnit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OtherItems'


class Outwardfiles(models.Model):
    outwardid = models.IntegerField(db_column='OutwardID')  # Field name made lowercase.
    outwardno = models.CharField(db_column='OutwardNo', primary_key=True, max_length=20)  # Field name made lowercase.
    fileno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='FileNo', blank=True, null=True)  # Field name made lowercase.
    takendatetime = models.DateTimeField(db_column='TakenDateTime', blank=True, null=True)  # Field name made lowercase.
    takenby = models.CharField(db_column='TakenBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    billaccountname = models.CharField(db_column='BillAccountName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OutwardFiles'


class Packageconsumption(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, PackageNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    packageno = models.ForeignKey('Packages', models.DO_NOTHING, db_column='PackageNo')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    packagevisitno = models.CharField(db_column='PackageVisitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemStatusID', related_name='packageconsumption_itemstatusid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PackageConsumption'
        unique_together = (('visitno', 'packageno', 'itemcode', 'itemcategoryid'),)


class Packagevisits(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, PackageNo) found, that is not supported. The first column is selected.
    patientno = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    packageno = models.ForeignKey('Packages', models.DO_NOTHING, db_column='PackageNo')  # Field name made lowercase.
    packagevisitno = models.CharField(db_column='PackageVisitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PackageVisits'
        unique_together = (('visitno', 'packageno'),)


class Packages(models.Model):
    packageid = models.IntegerField(db_column='PackageID')  # Field name made lowercase.
    packageno = models.CharField(db_column='PackageNo', primary_key=True, max_length=20)  # Field name made lowercase.
    packagename = models.CharField(db_column='PackageName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    expirydays = models.IntegerField(db_column='ExpiryDays', blank=True, null=True)  # Field name made lowercase.
    revenuestreamcode = models.ForeignKey('Revenuestreams', models.DO_NOTHING, db_column='RevenueStreamCode', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    monitorqty = models.BooleanField(db_column='MonitorQty', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    standardfee = models.DecimalField(db_column='StandardFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Packages'


class Packagesext(models.Model):
    packageno = models.OneToOneField(Packages, models.DO_NOTHING, db_column='PackageNo', primary_key=True)  # Field name made lowercase. The composite primary key (PackageNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PackagesEXT'
        unique_together = (('packageno', 'itemcode', 'itemcategoryid'),)


class Parishes(models.Model):
    parishcode = models.CharField(db_column='ParishCode', primary_key=True, max_length=20)  # Field name made lowercase.
    parishname = models.CharField(db_column='ParishName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    subcountycode = models.ForeignKey('Subcounties', models.DO_NOTHING, db_column='SubCountyCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parishes'
        unique_together = (('parishname', 'subcountycode'),)


class Pathologyexaminations(models.Model):
    examid = models.IntegerField(db_column='ExamID')  # Field name made lowercase.
    examcode = models.CharField(db_column='ExamCode', primary_key=True, max_length=20)  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    pathologycategoriesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PathologyCategoriesID', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PathologyExaminations'


class Pathologyimages(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ImageName) found, that is not supported. The first column is selected.
    imagename = models.CharField(db_column='ImageName', max_length=20)  # Field name made lowercase.
    pathologyimage = models.BinaryField(db_column='PathologyImage', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PathologyImages'
        unique_together = (('visitno', 'imagename'),)


class Pathologyreports(models.Model):
    visitno = models.OneToOneField(Items, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='pathologyreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='pathologyreports_itemcategoryid_set')  # Field name made lowercase.
    reporttypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReportTypeID', blank=True, null=True)  # Field name made lowercase.
    examdatetime = models.DateTimeField(db_column='ExamDateTime', blank=True, null=True)  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(db_column='Diagnosis', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    macroscopic = models.CharField(db_column='Macroscopic', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    microscopic = models.CharField(db_column='Microscopic', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    pathologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Pathologist', blank=True, null=True)  # Field name made lowercase.
    pathologytitleid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PathologyTitleID', related_name='pathologyreports_pathologytitleid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PathologyReports'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Patientallergies(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, AllergyNo) found, that is not supported. The first column is selected.
    allergyno = models.ForeignKey(Allergies, models.DO_NOTHING, db_column='AllergyNo')  # Field name made lowercase.
    reaction = models.CharField(db_column='Reaction', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientAllergies'
        unique_together = (('patientno', 'allergyno'),)


class Patientconsent(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fingerprintverified = models.BooleanField(db_column='FingerprintVerified', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientConsent'


class Patientrisks(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    riskfactors = models.CharField(db_column='RiskFactors', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientRisks'


class Patients(models.Model):
    patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
    patientno = models.CharField(db_column='PatientNo', primary_key=True, max_length=20)  # Field name made lowercase.
    nationalidno = models.CharField(db_column='NationalIDNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GenderID', blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    fingerprint = models.BinaryField(db_column='Fingerprint', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nokname = models.CharField(db_column='NOKName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    nokrelationship = models.CharField(db_column='NOKRelationship', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nokphone = models.CharField(db_column='NOKPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    defaultbillmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DefaultBillModesID', related_name='patients_defaultbillmodesid_set', blank=True, null=True)  # Field name made lowercase.
    defaultbillno = models.CharField(db_column='DefaultBillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    defaultmembercardno = models.CharField(db_column='DefaultMemberCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    defaultmainmembername = models.CharField(db_column='DefaultMainMemberName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    enforcedefaultbillno = models.BooleanField(db_column='EnforceDefaultBillNo')  # Field name made lowercase.
    hidedetails = models.BooleanField(db_column='HideDetails', blank=True, null=True)  # Field name made lowercase.
    statusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StatusID', related_name='patients_statusid_set', blank=True, null=True)  # Field name made lowercase.
    bloodgroupid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BloodGroupID', related_name='patients_bloodgroupid_set', blank=True, null=True)  # Field name made lowercase.
    villagecode = models.ForeignKey('Villages', models.DO_NOTHING, db_column='VillageCode', blank=True, null=True)  # Field name made lowercase.
    tribeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TribeID', related_name='patients_tribeid_set', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CountryID', related_name='patients_countryid_set', blank=True, null=True)  # Field name made lowercase.
    educationlevelid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EducationLevelID', related_name='patients_educationlevelid_set', blank=True, null=True)  # Field name made lowercase.
    maritalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MaritalStatusID', related_name='patients_maritalstatusid_set', blank=True, null=True)  # Field name made lowercase.
    careentrypointid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CareEntryPointID', related_name='patients_careentrypointid_set', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', related_name='patients_branchid_set', blank=True, null=True)  # Field name made lowercase.
    religionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReligionID', related_name='patients_religionid_set', blank=True, null=True)  # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=41, blank=True, null=True)  # Field name made lowercase.
    employeraddress = models.CharField(db_column='EmployerAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referringmedicalofficer = models.CharField(db_column='ReferringMedicalOfficer', max_length=41, blank=True, null=True)  # Field name made lowercase.
    nearestdispensary = models.CharField(db_column='NearestDispensary', max_length=30, blank=True, null=True)  # Field name made lowercase.
    previousadmissions = models.CharField(db_column='PreviousAdmissions', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chronicdiseases = models.CharField(db_column='ChronicDiseases', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firstvisitdate = models.DateTimeField(db_column='FirstVisitDate', blank=True, null=True)  # Field name made lowercase.
    lastvisitdate = models.DateTimeField(db_column='LastVisitDate', blank=True, null=True)  # Field name made lowercase.
    combinationon = models.CharField(db_column='CombinationOn', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totalvisits = models.IntegerField(db_column='TotalVisits', blank=True, null=True)  # Field name made lowercase.
    accountbalance = models.DecimalField(db_column='AccountBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    xraynumbers = models.DecimalField(db_column='XrayNumbers', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    policenotified = models.BooleanField(db_column='PoliceNotified')  # Field name made lowercase.
    infectiousdiseasesnotified = models.BooleanField(db_column='InfectiousDiseasesNotified')  # Field name made lowercase.
    referringfacility = models.CharField(db_column='ReferringFacility', max_length=41, blank=True, null=True)  # Field name made lowercase.
    medicalconditions = models.CharField(db_column='MedicalConditions', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(db_column='ProvisionalDiagnosis', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    communityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CommunityID', related_name='patients_communityid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    attachedtoid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AttachedToID', related_name='patients_attachedtoid_set', blank=True, null=True)  # Field name made lowercase.
    clientcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ClientCategoryID', related_name='patients_clientcategoryid_set', blank=True, null=True)  # Field name made lowercase.
    healthunitcode = models.ForeignKey(Healthunits, models.DO_NOTHING, db_column='HealthUnitCode', blank=True, null=True)  # Field name made lowercase.
    accountstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AccountStatusID', related_name='patients_accountstatusid_set', blank=True, null=True)  # Field name made lowercase.
    opdoutstanding = models.DecimalField(db_column='OPDOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    extrabilloutstanding = models.DecimalField(db_column='ExtraBillOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastaccountactiondate = models.DateTimeField(db_column='LastAccountActionDate', blank=True, null=True)  # Field name made lowercase.
    knowaboutservice = models.CharField(db_column='KnowAboutService', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tinnumber = models.CharField(db_column='TINNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patients'

    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Patientsext(models.Model):
    patientno = models.OneToOneField(Patients, models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, AlternateNo) found, that is not supported. The first column is selected.
    alternateno = models.CharField(db_column='AlternateNo', max_length=20)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alternatenoid = models.IntegerField(db_column='AlternateNoID', blank=True, null=True)  # Field name made lowercase.
    attachedtoid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AttachedToID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PatientsEXT'
        unique_together = (('patientno', 'alternateno'),)


class Paymentdetails(models.Model):
    receiptno = models.OneToOneField('Payments', models.DO_NOTHING, db_column='ReceiptNo', primary_key=True)  # Field name made lowercase. The composite primary key (ReceiptNo, VisitNo, ItemCode, ItemCategoryID, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey(Items, models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='paymentdetails_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='paymentdetails_itemcategoryid_set')  # Field name made lowercase.
    visittypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentDetails'
        unique_together = (('receiptno', 'visitno', 'itemcode', 'itemcategoryid', 'itemcategoryid'),)


class Paymentextrabillitems(models.Model):
    receiptno = models.OneToOneField('Payments', models.DO_NOTHING, db_column='ReceiptNo', primary_key=True)  # Field name made lowercase. The composite primary key (ReceiptNo, ExtraBillNo, ItemCode, ItemCategoryID, ItemCategoryID) found, that is not supported. The first column is selected.
    extrabillno = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    itemcode = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCode', related_name='paymentextrabillitems_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Extrabillitems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='paymentextrabillitems_itemcategoryid_set')  # Field name made lowercase.
    visittypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentExtraBillItems'
        unique_together = (('receiptno', 'extrabillno', 'itemcode', 'itemcategoryid', 'itemcategoryid'),)


class Paymentrequests(models.Model):
    payid = models.IntegerField(db_column='PayID', blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', primary_key=True, max_length=20)  # Field name made lowercase.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    paystatus = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayStatus', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentRequests'


class Paymentvoucherdetails(models.Model):
    voucherno = models.OneToOneField('Paymentvouchers', models.DO_NOTHING, db_column='VoucherNo', primary_key=True)  # Field name made lowercase. The composite primary key (VoucherNo, BillNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    billno = models.CharField(db_column='BillNo', max_length=20)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentVoucherDetails'
        unique_together = (('voucherno', 'billno', 'itemcode', 'itemcategoryid'),)


class Paymentvouchers(models.Model):
    voucherid = models.IntegerField(db_column='VoucherID')  # Field name made lowercase.
    voucherno = models.CharField(db_column='VoucherNo', primary_key=True, max_length=20)  # Field name made lowercase.
    paytypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayTypeID', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    paymodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayModesID', related_name='paymentvouchers_paymodesid_set', blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', related_name='paymentvouchers_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    amounttendered = models.DecimalField(db_column='AmountTendered', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sendbalancetoaccount = models.BooleanField(db_column='SendBalanceToAccount', blank=True, null=True)  # Field name made lowercase.
    useaccountbalance = models.BooleanField(db_column='UseAccountBalance', blank=True, null=True)  # Field name made lowercase.
    vouchertypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VoucherTypeID', related_name='paymentvouchers_vouchertypeid_set', blank=True, null=True)  # Field name made lowercase.
    payno = models.CharField(db_column='PayNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    filterno = models.CharField(db_column='FilterNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payee = models.CharField(db_column='Payee', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentVouchers'


class Payments(models.Model):
    receiptid = models.IntegerField(db_column='ReceiptID')  # Field name made lowercase.
    receiptno = models.CharField(db_column='ReceiptNo', primary_key=True, max_length=20)  # Field name made lowercase.
    paytypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayTypeID', blank=True, null=True)  # Field name made lowercase.
    payno = models.CharField(db_column='PayNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientfullname = models.CharField(db_column='ClientFullName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateTimeField(db_column='PayDate', blank=True, null=True)  # Field name made lowercase.
    paymodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayModesID', related_name='payments_paymodesid_set', blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', related_name='payments_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    withholdingtax = models.DecimalField(db_column='WithholdingTax', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    granddiscount = models.DecimalField(db_column='GrandDiscount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amounttendered = models.DecimalField(db_column='AmountTendered', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    change = models.DecimalField(db_column='Change', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sendbalancetoaccount = models.BooleanField(db_column='SendBalanceToAccount', blank=True, null=True)  # Field name made lowercase.
    useaccountbalance = models.BooleanField(db_column='UseAccountBalance', blank=True, null=True)  # Field name made lowercase.
    filterno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='FilterNo', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', related_name='payments_branchid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cashamount = models.DecimalField(db_column='CashAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'


class Pelvicexamination(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    ancno = models.ForeignKey(Antenatalenrollment, models.DO_NOTHING, db_column='ANCNo', blank=True, null=True)  # Field name made lowercase.
    vulvaid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VulvaID', blank=True, null=True)  # Field name made lowercase.
    cervixid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CervixID', related_name='pelvicexamination_cervixid_set', blank=True, null=True)  # Field name made lowercase.
    adnexaid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AdnexaID', related_name='pelvicexamination_adnexaid_set', blank=True, null=True)  # Field name made lowercase.
    vaginaid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VaginaID', related_name='pelvicexamination_vaginaid_set', blank=True, null=True)  # Field name made lowercase.
    uterusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='UterusID', related_name='pelvicexamination_uterusid_set', blank=True, null=True)  # Field name made lowercase.
    diagonalconjugate = models.IntegerField(db_column='DiagonalConjugate', blank=True, null=True)  # Field name made lowercase.
    sacralcurve = models.IntegerField(db_column='SacralCurve', blank=True, null=True)  # Field name made lowercase.
    ischialspine = models.IntegerField(db_column='IschialSpine', blank=True, null=True)  # Field name made lowercase.
    subpublicangle = models.IntegerField(db_column='SubPublicAngle', blank=True, null=True)  # Field name made lowercase.
    ischialtuberosities = models.IntegerField(db_column='IschialTuberosities', blank=True, null=True)  # Field name made lowercase.
    conclusionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ConclusionID', related_name='pelvicexamination_conclusionid_set', blank=True, null=True)  # Field name made lowercase.
    riskfactors = models.CharField(db_column='RiskFactors', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    recommendations = models.CharField(db_column='Recommendations', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PelvicExamination'


class Perinatal(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    modeofdelivery = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ModeOfDelivery', blank=True, null=True)  # Field name made lowercase.
    durationoflabour = models.DecimalField(db_column='DurationOfLabour', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deliverycomplications = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DeliveryComplications', related_name='perinatal_deliverycomplications_set', blank=True, null=True)  # Field name made lowercase.
    amountofbloodloss = models.DecimalField(db_column='AmountOfBloodLoss', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    motherscondition = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MothersCondition', related_name='perinatal_motherscondition_set', blank=True, null=True)  # Field name made lowercase.
    detailsofcondition = models.CharField(db_column='DetailsOfCondition', max_length=100, blank=True, null=True)  # Field name made lowercase.
    babyalive = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BabyAlive', related_name='perinatal_babyalive_set', blank=True, null=True)  # Field name made lowercase.
    causeofdeath = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CauseOfDeath', related_name='perinatal_causeofdeath_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Perinatal'


class Physicalstockcount(models.Model):
    pscid = models.IntegerField(db_column='PSCID')  # Field name made lowercase.
    pscno = models.CharField(db_column='PSCNo', primary_key=True, max_length=20)  # Field name made lowercase.
    generalnotes = models.CharField(db_column='GeneralNotes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    closed = models.BooleanField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysicalStockCount'


class Physicalstockcountdetails(models.Model):
    pscno = models.ForeignKey(Physicalstockcount, models.DO_NOTHING, db_column='PSCNo')  # Field name made lowercase.
    locationid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID', related_name='physicalstockcountdetails_itemcategoryid_set')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    systemquantity = models.IntegerField(db_column='SystemQuantity', blank=True, null=True)  # Field name made lowercase.
    physicalcountquantity = models.IntegerField(db_column='PhysicalCountQuantity', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=20, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800, blank=True, null=True)  # Field name made lowercase.
    stocktypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StockTypeID', related_name='physicalstockcountdetails_stocktypeid_set', blank=True, null=True)  # Field name made lowercase.
    stocktype = models.CharField(db_column='StockType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    variance = models.IntegerField(db_column='Variance', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysicalStockCountDetails'


class Physiodiagnosis(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, PhysioDiseaseNo) found, that is not supported. The first column is selected.
    physiodiseaseno = models.ForeignKey('Physiodiseases', models.DO_NOTHING, db_column='PhysioDiseaseNo')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysioDiagnosis'
        unique_together = (('visitno', 'physiodiseaseno'),)


class Physiodiseases(models.Model):
    diseaseid = models.IntegerField(db_column='DiseaseID', blank=True, null=True)  # Field name made lowercase.
    physiodiseaseno = models.CharField(db_column='PhysioDiseaseNo', primary_key=True, max_length=20)  # Field name made lowercase.
    diseasecode = models.CharField(db_column='DiseaseCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    diseasename = models.CharField(db_column='DiseaseName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    physiodiseasecategoriesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PhysioDiseaseCategoriesID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhysioDiseases'


class Physiotherapy(models.Model):
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo', blank=True, null=True)  # Field name made lowercase.
    onmedication = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='OnMedication', blank=True, null=True)  # Field name made lowercase.
    medication = models.CharField(db_column='Medication', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pain24hoursorvas = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Pain24hoursOrVAS', related_name='physiotherapy_pain24hoursorvas_set', blank=True, null=True)  # Field name made lowercase.
    levelofdependenceoradls = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='LevelOfDependenceOrADLS', related_name='physiotherapy_levelofdependenceoradls_set', blank=True, null=True)  # Field name made lowercase.
    musclestatus = models.CharField(db_column='MuscleStatus', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statusofjoints = models.CharField(db_column='StatusOfJoints', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sensitivity = models.CharField(db_column='Sensitivity', max_length=100, blank=True, null=True)  # Field name made lowercase.
    walkinganalysis = models.CharField(db_column='WalkingAnalysis', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shorttermtreatmenttargets = models.CharField(db_column='ShortTermTreatmentTargets', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longtermtreatmenttargets = models.CharField(db_column='LongTermTreatmentTargets', max_length=100, blank=True, null=True)  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(db_column='ProvisionalDiagnosis', max_length=100, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Physiotherapy'


class Policylimits(models.Model):
    companyno = models.OneToOneField(Insuranceschemes, models.DO_NOTHING, db_column='CompanyNo', primary_key=True)  # Field name made lowercase. The composite primary key (CompanyNo, PolicyNo, BenefitCode) found, that is not supported. The first column is selected.
    policyno = models.ForeignKey(Insuranceschemes, models.DO_NOTHING, db_column='PolicyNo', related_name='policylimits_policyno_set')  # Field name made lowercase.
    benefitcode = models.ForeignKey(Memberbenefits, models.DO_NOTHING, db_column='BenefitCode')  # Field name made lowercase.
    policylimit = models.DecimalField(db_column='PolicyLimit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PolicyLimits'
        unique_together = (('companyno', 'policyno', 'benefitcode'),)


class Possibleattacheditems(models.Model):
    objectno = models.CharField(db_column='ObjectNo', max_length=20)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.CharField(db_column='ItemCategoryID', max_length=10)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=20, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    objectdescription = models.CharField(db_column='ObjectDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PossibleAttachedItems'


class Postnatal(models.Model):
    patientno = models.ForeignKey(Patients, models.DO_NOTHING, db_column='PatientNo')  # Field name made lowercase.
    deliverycomplications = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DeliveryComplications', blank=True, null=True)  # Field name made lowercase.
    conditiononbirth = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ConditionOnBirth', related_name='postnatal_conditiononbirth_set', blank=True, null=True)  # Field name made lowercase.
    conditiondetails = models.CharField(db_column='ConditionDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    physicalabnormalitydetails = models.CharField(db_column='PhysicalAbnormalityDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    umblicalcorddetails = models.CharField(db_column='UmblicalCordDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jaundice = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Jaundice', related_name='postnatal_jaundice_set', blank=True, null=True)  # Field name made lowercase.
    earlyinfection = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EarlyInfection', related_name='postnatal_earlyinfection_set', blank=True, null=True)  # Field name made lowercase.
    infectiondetails = models.CharField(db_column='InfectionDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    convulsions = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Convulsions', related_name='postnatal_convulsions_set', blank=True, null=True)  # Field name made lowercase.
    convulsionsdetails = models.CharField(db_column='ConvulsionsDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eidresults = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EIDResults', related_name='postnatal_eidresults_set', blank=True, null=True)  # Field name made lowercase.
    apgarscore = models.IntegerField(db_column='ApgarScore', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PostNatal'


class Preoperative(models.Model):
    roundno = models.CharField(db_column='RoundNo', primary_key=True, max_length=20)  # Field name made lowercase.
    explainationofsurgery = models.BooleanField(db_column='ExplainationOfSurgery', blank=True, null=True)  # Field name made lowercase.
    bathed = models.BooleanField(db_column='Bathed', blank=True, null=True)  # Field name made lowercase.
    knownallergy = models.BooleanField(db_column='KnownAllergy', blank=True, null=True)  # Field name made lowercase.
    correctidentity = models.BooleanField(db_column='CorrectIdentity', blank=True, null=True)  # Field name made lowercase.
    correctnotes = models.BooleanField(db_column='CorrectNotes', blank=True, null=True)  # Field name made lowercase.
    npmlast6hrs = models.BooleanField(db_column='NPMLast6hrs', blank=True, null=True)  # Field name made lowercase.
    consentsigned = models.BooleanField(db_column='ConsentSigned', blank=True, null=True)  # Field name made lowercase.
    denturesremoved = models.BooleanField(db_column='DenturesRemoved', blank=True, null=True)  # Field name made lowercase.
    jewelleryremoved = models.BooleanField(db_column='JewelleryRemoved', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preoperative'


class Printdetails(models.Model):
    patientno = models.CharField(db_column='PatientNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (PatientNo, PrintDesc, RecordDateTime) found, that is not supported. The first column is selected.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    printdesc = models.CharField(db_column='PrintDesc', max_length=200)  # Field name made lowercase.
    printcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PrintCategoryID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrintDetails'
        unique_together = (('patientno', 'printdesc', 'recorddatetime'),)


class Priorartdetails(models.Model):
    patientno = models.OneToOneField(Patients, models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, PriorARTID) found, that is not supported. The first column is selected.
    priorartid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PriorARTID')  # Field name made lowercase.
    artdate = models.DateTimeField(db_column='ARTDate', blank=True, null=True)  # Field name made lowercase.
    artwhere = models.CharField(db_column='ARTWhere', max_length=41, blank=True, null=True)  # Field name made lowercase.
    combination = models.ForeignKey(Drugcombinations, models.DO_NOTHING, db_column='Combination', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriorARTDetails'
        unique_together = (('patientno', 'priorartid'),)


class Procedures(models.Model):
    procedureid = models.IntegerField(db_column='ProcedureID')  # Field name made lowercase.
    procedurecode = models.CharField(db_column='ProcedureCode', primary_key=True, max_length=10)  # Field name made lowercase.
    procedurename = models.CharField(db_column='ProcedureName', unique=True, max_length=800, blank=True, null=True)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    procedurecategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ProcedureCategoryID', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    revenuestream = models.CharField(db_column='RevenueStream', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Procedures'


class Productownerinfo(models.Model):
    productowner = models.CharField(db_column='ProductOwner', primary_key=True, max_length=200)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alternatephone = models.CharField(db_column='AlternatePhone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alternateemail = models.CharField(db_column='AlternateEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    alternatephoto = models.BinaryField(db_column='AlternatePhoto', blank=True, null=True)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tinno = models.CharField(db_column='TINNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    printheaderalignmentid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PrintHeaderAlignmentID', blank=True, null=True)  # Field name made lowercase.
    logotopmargin = models.SmallIntegerField(db_column='LogoTopMargin', blank=True, null=True)  # Field name made lowercase.
    texttopmargin = models.SmallIntegerField(db_column='TextTopMargin', blank=True, null=True)  # Field name made lowercase.
    logoleftmargin = models.SmallIntegerField(db_column='LogoLeftMargin', blank=True, null=True)  # Field name made lowercase.
    textleftmargin = models.SmallIntegerField(db_column='TextLeftMargin', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductOwnerInfo'


class Purchaseorderdetails(models.Model):
    purchaseorderno = models.OneToOneField('Purchaseorders', models.DO_NOTHING, db_column='PurchaseOrderNo', primary_key=True)  # Field name made lowercase. The composite primary key (PurchaseOrderNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemgroup = models.CharField(db_column='ItemGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    packid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PackID', related_name='purchaseorderdetails_packid_set')  # Field name made lowercase.
    packsize = models.IntegerField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatvalue = models.DecimalField(db_column='VATValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stockstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StockStatusID', related_name='purchaseorderdetails_stockstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrderDetails'
        unique_together = (('purchaseorderno', 'itemcategoryid', 'itemcode'), ('purchaseorderno', 'itemcategoryid', 'itemname'),)


class Purchaseorders(models.Model):
    purchaseorderid = models.IntegerField(db_column='PurchaseOrderID')  # Field name made lowercase.
    purchaseorderno = models.CharField(db_column='PurchaseOrderNo', primary_key=True, max_length=20)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplierno = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierNo', blank=True, null=True)  # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=300, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrders'


class Queuedmessages(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, BranchID, ServicePointID) found, that is not supported. The first column is selected.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    roomnameid = models.CharField(db_column='RoomNameID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicepointid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ServicePointID', related_name='queuedmessages_servicepointid_set')  # Field name made lowercase.
    tokenno = models.CharField(db_column='TokenNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    readcount = models.IntegerField(db_column='ReadCount', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QueuedMessages'
        unique_together = (('visitno', 'branchid', 'servicepointid'),)


class Queues(models.Model):
    tokenid = models.IntegerField(db_column='TokenID')  # Field name made lowercase.
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, BranchID, ServicePointID) found, that is not supported. The first column is selected.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID')  # Field name made lowercase.
    servicepointid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ServicePointID', related_name='queues_servicepointid_set')  # Field name made lowercase.
    tokenno = models.CharField(db_column='TokenNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    priorityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PriorityID', related_name='queues_priorityid_set', blank=True, null=True)  # Field name made lowercase.
    queuestatus = models.BooleanField(db_column='QueueStatus', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Queues'
        unique_together = (('visitno', 'branchid', 'servicepointid'),)


class Quicksearchcolumns(models.Model):
    sortorder = models.AutoField(primary_key=True, db_column='SortOrder')  # Field name made lowercase.
    objectname = models.OneToOneField('Searchobjects', models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase. The composite primary key (ObjectName, ColumnName) found, that is not supported. The first column is selected.
    columnname = models.CharField(db_column='ColumnName', max_length=200)  # Field name made lowercase.
    columncaption = models.CharField(db_column='ColumnCaption', max_length=200)  # Field name made lowercase.
    columnreference = models.CharField(db_column='ColumnReference', max_length=200)  # Field name made lowercase.
    searchcriterionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SearchCriterionID')  # Field name made lowercase.
    searchable = models.BooleanField(db_column='Searchable', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuickSearchColumns'
        unique_together = (('objectname', 'columnname'), ('objectname', 'columncaption'), ('objectname', 'columnreference'),)


class Quotationdetails(models.Model):
    quotationno = models.OneToOneField('Quotations', models.DO_NOTHING, db_column='QuotationNo', primary_key=True)  # Field name made lowercase. The composite primary key (QuotationNo, VisitNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    visitno = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitNo')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    discount = models.DecimalField(db_column='Discount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuotationDetails'
        unique_together = (('quotationno', 'visitno', 'itemcategoryid', 'itemcode'), ('quotationno', 'visitno', 'itemcategoryid', 'itemname'),)


class Quotations(models.Model):
    quotationid = models.IntegerField(db_column='QuotationID')  # Field name made lowercase.
    quotationno = models.CharField(db_column='QuotationNo', primary_key=True, max_length=20)  # Field name made lowercase.
    quotationdate = models.DateTimeField(db_column='QuotationDate', blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Quotations'


class Radiologyexaminations(models.Model):
    examid = models.IntegerField(db_column='ExamID')  # Field name made lowercase.
    examcode = models.CharField(db_column='ExamCode', primary_key=True, max_length=20)  # Field name made lowercase.
    examname = models.CharField(db_column='ExamName', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    radiologycategoriesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='RadiologyCategoriesID', blank=True, null=True)  # Field name made lowercase.
    radiologysiteid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='RadiologySiteID', related_name='radiologyexaminations_radiologysiteid_set', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RadiologyExaminations'


class Radiologyreports(models.Model):
    visitno = models.OneToOneField(Items, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    itemcode = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCode', related_name='radiologyreports_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Items, models.DO_NOTHING, db_column='ItemCategoryID', related_name='radiologyreports_itemcategoryid_set')  # Field name made lowercase.
    examdatetime = models.DateTimeField(db_column='ExamDateTime', blank=True, null=True)  # Field name made lowercase.
    indication = models.CharField(db_column='Indication', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    radiologist = models.ForeignKey('Staff', models.DO_NOTHING, db_column='Radiologist', blank=True, null=True)  # Field name made lowercase.
    radiologytitleid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='RadiologyTitleID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RadiologyReports'
        unique_together = (('visitno', 'itemcode', 'itemcategoryid'),)


class Receiptreversals(models.Model):
    receiptno = models.ForeignKey(Payments, models.DO_NOTHING, db_column='ReceiptNo', blank=True, null=True)  # Field name made lowercase.
    refundno = models.OneToOneField('Refunds', models.DO_NOTHING, db_column='RefundNo', primary_key=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReceiptReversals'


class Referrals(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    referraldate = models.DateTimeField(db_column='ReferralDate', blank=True, null=True)  # Field name made lowercase.
    referredby = models.ForeignKey('Staff', models.DO_NOTHING, db_column='ReferredBy', blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID', blank=True, null=True)  # Field name made lowercase.
    referredto = models.ForeignKey('Staff', models.DO_NOTHING, db_column='ReferredTo', related_name='referrals_referredto_set', blank=True, null=True)  # Field name made lowercase.
    referralnotes = models.CharField(db_column='ReferralNotes', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referrals'


class Refraction(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    rightmrsph = models.CharField(db_column='RightMRSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftmrsph = models.CharField(db_column='LeftMRSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightmrcyl = models.CharField(db_column='RightMRCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftmrcyl = models.CharField(db_column='LeftMRCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightmraxis = models.CharField(db_column='RightMRAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftmraxis = models.CharField(db_column='LeftMRAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightcrsph = models.CharField(db_column='RightCRSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftcrsph = models.CharField(db_column='LeftCRSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightcrcyl = models.CharField(db_column='RightCRCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftcrcyl = models.CharField(db_column='LeftCRCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightcraxis = models.CharField(db_column='RightCRAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftcraxis = models.CharField(db_column='LeftCRAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightpcrsph = models.CharField(db_column='RightPCRSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftpcrsph = models.CharField(db_column='LeftPCRSPH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightpcrcyl = models.CharField(db_column='RightPCRCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftpcrcyl = models.CharField(db_column='LeftPCRCYL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rightpcraxis = models.CharField(db_column='RightPCRAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leftpcrraxis = models.CharField(db_column='LeftPCRRAXIS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pd = models.CharField(db_column='PD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    segmentheights = models.CharField(db_column='SegmentHeights', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Refraction'


class Refundapprovals(models.Model):
    refundrequestno = models.OneToOneField('Refundrequests', models.DO_NOTHING, db_column='RefundRequestNo', primary_key=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=800, blank=True, null=True)  # Field name made lowercase.
    attendingpersonel = models.CharField(db_column='AttendingPersonel', max_length=41, blank=True, null=True)  # Field name made lowercase.
    approvalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ApprovalStatusID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundApprovals'


class Refunddetails(models.Model):
    refundno = models.OneToOneField('Refunds', models.DO_NOTHING, db_column='RefundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RefundNo, VisitNo, ReceiptNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.CharField(db_column='VisitNo', max_length=20)  # Field name made lowercase.
    receiptno = models.CharField(db_column='ReceiptNo', max_length=20)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    returnreasonid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReturnReasonID', related_name='refunddetails_returnreasonid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundDetails'
        unique_together = (('refundno', 'visitno', 'receiptno', 'itemcode', 'itemcategoryid'),)


class Refundextrabillitems(models.Model):
    refundno = models.OneToOneField('Refunds', models.DO_NOTHING, db_column='RefundNo', primary_key=True)  # Field name made lowercase. The composite primary key (RefundNo, ExtraBillNo, ReceiptNo, ItemCode, ItemCategoryID, ItemCategoryID) found, that is not supported. The first column is selected.
    extrabillno = models.ForeignKey(Paymentextrabillitems, models.DO_NOTHING, db_column='ExtraBillNo')  # Field name made lowercase.
    receiptno = models.ForeignKey(Paymentextrabillitems, models.DO_NOTHING, db_column='ReceiptNo', related_name='refundextrabillitems_receiptno_set')  # Field name made lowercase.
    itemcode = models.ForeignKey(Paymentextrabillitems, models.DO_NOTHING, db_column='ItemCode', related_name='refundextrabillitems_itemcode_set')  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Paymentextrabillitems, models.DO_NOTHING, db_column='ItemCategoryID', related_name='refundextrabillitems_itemcategoryid_set')  # Field name made lowercase.
    returnreasonid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReturnReasonID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundExtraBillItems'
        unique_together = (('refundno', 'extrabillno', 'receiptno', 'itemcode', 'itemcategoryid', 'itemcategoryid'),)


class Refundrejects(models.Model):
    refundrequestno = models.OneToOneField('Refundrequests', models.DO_NOTHING, db_column='RefundRequestNo', primary_key=True)  # Field name made lowercase.
    receiptno = models.ForeignKey(Payments, models.DO_NOTHING, db_column='ReceiptNo', blank=True, null=True)  # Field name made lowercase.
    rejectedat = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='RejectedAt', blank=True, null=True)  # Field name made lowercase.
    rejectiondate = models.DateTimeField(db_column='RejectionDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundRejects'


class Refundrequestdetails(models.Model):
    refundrequestno = models.OneToOneField('Refundrequests', models.DO_NOTHING, db_column='RefundRequestNo', primary_key=True)  # Field name made lowercase. The composite primary key (RefundRequestNo, VisitNo, ReceiptNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    visitno = models.CharField(db_column='VisitNo', max_length=20)  # Field name made lowercase.
    receiptno = models.CharField(db_column='ReceiptNo', max_length=20)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    returnreasonid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReturnReasonID', related_name='refundrequestdetails_returnreasonid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    newprice = models.DecimalField(db_column='NewPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundRequestDetails'
        unique_together = (('refundrequestno', 'visitno', 'receiptno', 'itemcode', 'itemcategoryid'),)


class Refundrequestextrabillitems(models.Model):
    refundrequestno = models.OneToOneField('Refundrequests', models.DO_NOTHING, db_column='RefundRequestNo', primary_key=True)  # Field name made lowercase. The composite primary key (RefundRequestNo, ExtraBillNo, ReceiptNo, ItemCode, ItemCategoryID) found, that is not supported. The first column is selected.
    extrabillno = models.CharField(db_column='ExtraBillNo', max_length=20)  # Field name made lowercase.
    receiptno = models.CharField(db_column='ReceiptNo', max_length=20)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    returnreasonid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReturnReasonID', related_name='refundrequestextrabillitems_returnreasonid_set', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    newprice = models.DecimalField(db_column='NewPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundRequestExtraBillItems'
        unique_together = (('refundrequestno', 'extrabillno', 'receiptno', 'itemcode', 'itemcategoryid'),)


class Refundrequests(models.Model):
    refundrequestid = models.IntegerField(db_column='RefundRequestID')  # Field name made lowercase.
    refundrequestno = models.CharField(db_column='RefundRequestNo', primary_key=True, max_length=20)  # Field name made lowercase.
    receiptno = models.ForeignKey(Payments, models.DO_NOTHING, db_column='ReceiptNo', blank=True, null=True)  # Field name made lowercase.
    requeststatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='RequestStatusID', blank=True, null=True)  # Field name made lowercase.
    approvalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ApprovalStatusID', related_name='refundrequests_approvalstatusid_set', blank=True, null=True)  # Field name made lowercase.
    requestedby = models.CharField(db_column='Requestedby', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RefundRequests'


class Refunds(models.Model):
    refundid = models.IntegerField(db_column='RefundID')  # Field name made lowercase.
    refundno = models.CharField(db_column='RefundNo', primary_key=True, max_length=20)  # Field name made lowercase.
    receiptno = models.ForeignKey(Payments, models.DO_NOTHING, db_column='ReceiptNo', blank=True, null=True)  # Field name made lowercase.
    refundrequestno = models.ForeignKey(Refundrequests, models.DO_NOTHING, db_column='RefundRequestNo', blank=True, null=True)  # Field name made lowercase.
    refunddate = models.DateTimeField(db_column='RefundDate', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Refunds'


class Rejectedspecimens(models.Model):
    specimenno = models.CharField(db_column='SpecimenNo', primary_key=True, max_length=20)  # Field name made lowercase.
    visitno = models.CharField(db_column='VisitNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rejectectionreasonid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='RejectectionReasonID', blank=True, null=True)  # Field name made lowercase.
    rejectiondate = models.DateTimeField(db_column='RejectionDate', blank=True, null=True)  # Field name made lowercase.
    rejectedat = models.CharField(db_column='RejectedAt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rejectedby = models.CharField(db_column='RejectedBy', max_length=40, blank=True, null=True)  # Field name made lowercase.
    isreaccepted = models.BooleanField(db_column='IsReAccepted', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RejectedSpecimens'


class Researchpatientsenrollment(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    researchnameid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ResearchNameID', blank=True, null=True)  # Field name made lowercase.
    researchstartdate = models.DateTimeField(db_column='ResearchStartDate', blank=True, null=True)  # Field name made lowercase.
    principleinvestigator = models.ForeignKey('Staff', models.DO_NOTHING, db_column='PrincipleInvestigator', blank=True, null=True)  # Field name made lowercase.
    activestatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ActiveStatusID', related_name='researchpatientsenrollment_activestatusid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResearchPatientsEnrollment'


class Researchpatientsstop(models.Model):
    visitno = models.OneToOneField(Researchpatientsenrollment, models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    researchenddate = models.DateTimeField(db_column='ResearchEndDate', blank=True, null=True)  # Field name made lowercase.
    outcome = models.CharField(db_column='OutCome', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResearchPatientsStop'


class Researchroutingform(models.Model):
    ucino = models.IntegerField(db_column='UCINo', blank=True, null=True)  # Field name made lowercase.
    uciid = models.CharField(db_column='UCIID', primary_key=True, max_length=20)  # Field name made lowercase.
    patientno = models.CharField(db_column='PatientNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    othername = models.CharField(db_column='OtherName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    referalinitials = models.CharField(db_column='ReferalInitials', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GenderID', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    villagecode = models.ForeignKey('Villages', models.DO_NOTHING, db_column='VillageCode', blank=True, null=True)  # Field name made lowercase.
    referraldate = models.DateTimeField(db_column='ReferralDate', blank=True, null=True)  # Field name made lowercase.
    referralstudycodeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReferralStudyCodeID', related_name='researchroutingform_referralstudycodeid_set', blank=True, null=True)  # Field name made lowercase.
    referralstudyname = models.CharField(db_column='ReferralStudyName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(db_column='Diagnosis', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    healthunitcode = models.ForeignKey(Healthunits, models.DO_NOTHING, db_column='HealthUnitCode', blank=True, null=True)  # Field name made lowercase.
    referredby = models.CharField(db_column='ReferredBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    patientscreenedby = models.CharField(db_column='PatientScreenedBy', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referralinitials = models.CharField(db_column='ReferralInitials', max_length=10, blank=True, null=True)  # Field name made lowercase.
    eligibleforscreeningid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EligibleForScreeningID', related_name='researchroutingform_eligibleforscreeningid_set', blank=True, null=True)  # Field name made lowercase.
    exclusionreason = models.CharField(db_column='ExclusionReason', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    patientreferedto = models.CharField(db_column='PatientReferedTo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referreddate = models.DateTimeField(db_column='ReferredDate', blank=True, null=True)  # Field name made lowercase.
    scrno = models.CharField(db_column='SCRNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pid = models.CharField(db_column='PID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResearchRoutingForm'


class Resourcesint(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (Code, ItemCategoryID) found, that is not supported. The first column is selected.
    description = models.CharField(db_column='Description', max_length=10, blank=True, null=True)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    agent = models.CharField(db_column='Agent', max_length=10, blank=True, null=True)  # Field name made lowercase.
    syncstatus = models.BooleanField(db_column='SyncStatus', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResourcesINT'
        unique_together = (('code', 'itemcategoryid'),)


class Restrictedkeys(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName', primary_key=True)  # Field name made lowercase. The composite primary key (ObjectName, ColumnName) found, that is not supported. The first column is selected.
    columnname = models.CharField(db_column='ColumnName', max_length=60)  # Field name made lowercase.
    columncaption = models.CharField(db_column='ColumnCaption', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestrictedKeys'
        unique_together = (('objectname', 'columnname'),)


class Revenuestreams(models.Model):
    revenuestreamcode = models.CharField(db_column='RevenueStreamCode', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RevenueStreams'


class Roles(models.Model):
    rolename = models.CharField(db_column='RoleName', primary_key=True, max_length=40)  # Field name made lowercase.
    roledes = models.CharField(db_column='RoleDes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inbuilt = models.BooleanField(db_column='InBuilt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Rooms(models.Model):
    roomno = models.CharField(db_column='RoomNo', primary_key=True, max_length=20)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    wardsid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='WardsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rooms'
        unique_together = (('roomname', 'wardsid'),)


class Schememembers(models.Model):
    medicalcardid = models.IntegerField(db_column='MedicalCardID')  # Field name made lowercase.
    mainmemberid = models.IntegerField(db_column='MainMemberID')  # Field name made lowercase.
    membertypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MemberTypeID', blank=True, null=True)  # Field name made lowercase.
    medicalcardno = models.CharField(db_column='MedicalCardNo', primary_key=True, max_length=20)  # Field name made lowercase.
    mainmemberno = models.ForeignKey('self', models.DO_NOTHING, db_column='MainMemberNo', blank=True, null=True)  # Field name made lowercase.
    companyno = models.ForeignKey(Insuranceschemes, models.DO_NOTHING, db_column='CompanyNo', blank=True, null=True)  # Field name made lowercase.
    policyno = models.ForeignKey(Insuranceschemes, models.DO_NOTHING, db_column='PolicyNo', related_name='schememembers_policyno_set', blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GenderID', related_name='schememembers_genderid_set', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    phonework = models.CharField(db_column='PhoneWork', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phonemobile = models.CharField(db_column='PhoneMobile', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phonehome = models.CharField(db_column='PhoneHome', max_length=30, blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    fingerprint = models.BinaryField(db_column='Fingerprint', blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=41, blank=True, null=True)  # Field name made lowercase.
    policystartdate = models.DateTimeField(db_column='PolicyStartDate', blank=True, null=True)  # Field name made lowercase.
    policyenddate = models.DateTimeField(db_column='PolicyEndDate', blank=True, null=True)  # Field name made lowercase.
    memberstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MemberStatusID', related_name='schememembers_memberstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    memberpremium = models.DecimalField(db_column='MemberPremium', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    memberconsumption = models.DecimalField(db_column='MemberConsumption', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    memberbalance = models.DecimalField(db_column='MemberBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SchemeMembers'


class Searchcolumns(models.Model):
    sortorder = models.AutoField(primary_key=True, db_column='SortOrder')  # Field name made lowercase.
    objectname = models.ForeignKey('Searchobjects', models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase.
    columnname = models.CharField(db_column='ColumnName', max_length=200)  # Field name made lowercase. The composite primary key (ColumnName, ObjectName) found, that is not supported. The first column is selected.
    columncaption = models.CharField(db_column='ColumnCaption', max_length=200)  # Field name made lowercase.
    includeinitially = models.BooleanField(db_column='IncludeInitially', blank=True, null=True)  # Field name made lowercase.
    searchable = models.BooleanField(db_column='Searchable', blank=True, null=True)  # Field name made lowercase.
    isaggregate = models.BooleanField(db_column='IsAggregate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SearchColumns'
        unique_together = (('columnname', 'objectname'),)


class Searchcolumnsext(models.Model):
    objectname = models.ForeignKey(Searchcolumns, models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase.
    columnname = models.OneToOneField(Searchcolumns, models.DO_NOTHING, db_column='ColumnName', primary_key=True, related_name='searchcolumnsext_columnname_set')  # Field name made lowercase. The composite primary key (ColumnName, ObjectName) found, that is not supported. The first column is selected.
    searchcriterionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SearchCriterionID')  # Field name made lowercase.
    searchdatatypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SearchDataTypeID', related_name='searchcolumnsext_searchdatatypeid_set')  # Field name made lowercase.
    maxlength = models.SmallIntegerField(db_column='MaxLength', blank=True, null=True)  # Field name made lowercase.
    isprimarykey = models.BooleanField(db_column='IsPrimaryKey', blank=True, null=True)  # Field name made lowercase.
    searchcriterionlocked = models.BooleanField(db_column='SearchCriterionLocked', blank=True, null=True)  # Field name made lowercase.
    incolumns = models.BooleanField(db_column='InColumns', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SearchColumnsEXT'
        unique_together = (('columnname', 'objectname'),)


class Searchobjects(models.Model):
    sortorder = models.AutoField(primary_key=True, db_column='SortOrder')  # Field name made lowercase.
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName')  # Field name made lowercase.
    sp_name = models.CharField(db_column='SP_Name', max_length=60)  # Field name made lowercase.
    joinstext = models.CharField(db_column='JoinsText', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    isgrouped = models.BooleanField(db_column='IsGrouped', blank=True, null=True)  # Field name made lowercase.
    hasdefault = models.BooleanField(db_column='HasDefault', blank=True, null=True)  # Field name made lowercase.
    topvalue = models.SmallIntegerField(db_column='TopValue', blank=True, null=True)  # Field name made lowercase.
    ordercolumns = models.CharField(db_column='OrderColumns', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    isdistinct = models.BooleanField(db_column='IsDistinct')  # Field name made lowercase.
    searhinclude = models.BooleanField(db_column='SearhInclude')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SearchObjects'


class Searchqueries(models.Model):
    queryname = models.CharField(db_column='QueryName', primary_key=True, max_length=40)  # Field name made lowercase.
    objectname = models.ForeignKey(Accessobjects, models.DO_NOTHING, db_column='ObjectName', blank=True, null=True)  # Field name made lowercase.
    querydata = models.TextField(db_column='QueryData', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SearchQueries'


class Servercredentials(models.Model):
    sourcename = models.CharField(db_column='SourceName', primary_key=True, max_length=60)  # Field name made lowercase.
    connectionmodeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ConnectionModeID', blank=True, null=True)  # Field name made lowercase.
    sourcelogin = models.CharField(db_column='SourceLogin', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sourcepassword = models.CharField(db_column='SourcePassword', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServerCredentials'


class Serviceinvoicedetails(models.Model):
    serviceinvoiceno = models.OneToOneField('Serviceinvoices', models.DO_NOTHING, db_column='ServiceInvoiceNo', primary_key=True)  # Field name made lowercase. The composite primary key (ServiceInvoiceNo, ItemCategoryID, ItemCode) found, that is not supported. The first column is selected.
    itemcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=20)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=800)  # Field name made lowercase.
    unitmeasure = models.CharField(db_column='UnitMeasure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemgroup = models.CharField(db_column='ItemGroup', max_length=100, blank=True, null=True)  # Field name made lowercase.
    packid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PackID', related_name='serviceinvoicedetails_packid_set')  # Field name made lowercase.
    packsize = models.IntegerField(db_column='PackSize', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatvalue = models.DecimalField(db_column='VATValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    paystatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayStatusID', related_name='serviceinvoicedetails_paystatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceInvoiceDetails'
        unique_together = (('serviceinvoiceno', 'itemcategoryid', 'itemcode'), ('serviceinvoiceno', 'itemcategoryid', 'itemname'),)


class Serviceinvoices(models.Model):
    serviceinvoiceid = models.IntegerField(db_column='ServiceInvoiceID')  # Field name made lowercase.
    serviceinvoiceno = models.CharField(db_column='ServiceInvoiceNo', primary_key=True, max_length=20)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplierno = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierNo', blank=True, null=True)  # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=300, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceInvoices'


class Services(models.Model):
    serviceid = models.IntegerField(db_column='ServiceID')  # Field name made lowercase.
    servicecode = models.CharField(db_column='ServiceCode', primary_key=True, max_length=10)  # Field name made lowercase.
    servicename = models.CharField(db_column='ServiceName', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    servicepointid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ServicePointID', blank=True, null=True)  # Field name made lowercase.
    servicebillatid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ServiceBillAtID', related_name='services_servicebillatid_set', blank=True, null=True)  # Field name made lowercase.
    revenuestreamcode = models.CharField(db_column='RevenueStreamCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    standardfee = models.DecimalField(db_column='StandardFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    servicecategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ServiceCategoryID', related_name='services_servicecategoryid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Services'


class Servicesdrspecialtyfee(models.Model):
    servicecode = models.OneToOneField(Services, models.DO_NOTHING, db_column='ServiceCode', primary_key=True)  # Field name made lowercase. The composite primary key (ServiceCode, DoctorSpecialtyID) found, that is not supported. The first column is selected.
    doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID')  # Field name made lowercase.
    specialtyfee = models.DecimalField(db_column='SpecialtyFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', related_name='servicesdrspecialtyfee_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicesDrSpecialtyFee'
        unique_together = (('servicecode', 'doctorspecialtyid'),)


class Servicesspecialtybillcustomfee(models.Model):
    servicecode = models.OneToOneField(Services, models.DO_NOTHING, db_column='ServiceCode', primary_key=True)  # Field name made lowercase. The composite primary key (ServiceCode, DoctorSpecialtyID, AccountNo) found, that is not supported. The first column is selected.
    doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID')  # Field name made lowercase.
    accountno = models.ForeignKey(Billcustomers, models.DO_NOTHING, db_column='AccountNo')  # Field name made lowercase.
    customfee = models.DecimalField(db_column='CustomFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', related_name='servicesspecialtybillcustomfee_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicesSpecialtyBillCustomFee'
        unique_together = (('servicecode', 'doctorspecialtyid', 'accountno'),)


class Servicesspecialtycustomcode(models.Model):
    servicecode = models.OneToOneField(Services, models.DO_NOTHING, db_column='ServiceCode', primary_key=True)  # Field name made lowercase. The composite primary key (ServiceCode, DoctorSpecialtyID) found, that is not supported. The first column is selected.
    doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID')  # Field name made lowercase.
    customcode = models.CharField(db_column='CustomCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicesSpecialtyCustomCode'
        unique_together = (('servicecode', 'doctorspecialtyid'),)


class Servicesstaffbillcustomfee(models.Model):
    servicecode = models.OneToOneField(Services, models.DO_NOTHING, db_column='ServiceCode', primary_key=True)  # Field name made lowercase. The composite primary key (ServiceCode, StaffNo, AccountNo) found, that is not supported. The first column is selected.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo')  # Field name made lowercase.
    accountno = models.ForeignKey(Billcustomers, models.DO_NOTHING, db_column='AccountNo')  # Field name made lowercase.
    customfee = models.DecimalField(db_column='CustomFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicesStaffBillCustomFee'
        unique_together = (('servicecode', 'staffno', 'accountno'),)


class Servicesstafffee(models.Model):
    servicecode = models.OneToOneField(Services, models.DO_NOTHING, db_column='ServiceCode', primary_key=True)  # Field name made lowercase. The composite primary key (ServiceCode, StaffNo) found, that is not supported. The first column is selected.
    staffno = models.ForeignKey('Staff', models.DO_NOTHING, db_column='StaffNo')  # Field name made lowercase.
    stafffee = models.DecimalField(db_column='StaffFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicesStaffFee'
        unique_together = (('servicecode', 'staffno'),)


class Smartcardauthorisations(models.Model):
    patientno = models.OneToOneField(Patients, models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase. The composite primary key (PatientNo, BillModesID, BillNo, ToVisitDate) found, that is not supported. The first column is selected.
    billmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BillModesID')  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20)  # Field name made lowercase.
    tovisitdate = models.DateTimeField(db_column='ToVisitDate')  # Field name made lowercase.
    medicalcardno = models.CharField(db_column='MedicalCardNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    authorisedby = models.CharField(db_column='AuthorisedBy', max_length=41, blank=True, null=True)  # Field name made lowercase.
    authorisationreason = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AuthorisationReason', related_name='smartcardauthorisations_authorisationreason_set', blank=True, null=True)  # Field name made lowercase.
    claimreferenceno = models.CharField(db_column='ClaimReferenceNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SmartCardAuthorisations'
        unique_together = (('patientno', 'billmodesid', 'billno', 'tovisitdate'),)


class Specialedits(models.Model):
    objectname = models.OneToOneField(Accessobjects, models.DO_NOTHING, db_column='ObjectName', primary_key=True)  # Field name made lowercase.
    keycolumnname = models.CharField(db_column='KeyColumnName', max_length=100)  # Field name made lowercase.
    keycolumncaption = models.CharField(db_column='KeyColumnCaption', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpecialEdits'


class Staff(models.Model):
    staffid = models.IntegerField(db_column='StaffID')  # Field name made lowercase.
    staffno = models.CharField(db_column='StaffNo', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GenderID', blank=True, null=True)  # Field name made lowercase.
    stafftitleid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StaffTitleID', related_name='staff_stafftitleid_set', blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(db_column='Speciality', max_length=20, blank=True, null=True)  # Field name made lowercase.
    qualifications = models.CharField(db_column='Qualifications', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=40, blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID', related_name='staff_doctorspecialtyid_set', blank=True, null=True)  # Field name made lowercase.
    fingerprint = models.BinaryField(db_column='Fingerprint', blank=True, null=True)  # Field name made lowercase.
    signature = models.BinaryField(db_column='Signature', blank=True, null=True)  # Field name made lowercase.
    creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    creatorloginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='CreatorLoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', related_name='staff_loginid_set', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class Stafflocations(models.Model):
    staffloginid = models.OneToOneField(Logins, models.DO_NOTHING, db_column='StaffLoginID', primary_key=True)  # Field name made lowercase. The composite primary key (StaffLoginID, LocationID, StartDate) found, that is not supported. The first column is selected.
    locationid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='LocationID')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', related_name='stafflocations_loginid_set', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffLocations'
        unique_together = (('staffloginid', 'locationid', 'startdate'),)


class Staffpayments(models.Model):
    paymentvoucherid = models.IntegerField(db_column='PaymentVoucherID')  # Field name made lowercase.
    paymentvoucherno = models.CharField(db_column='PaymentVoucherNo', primary_key=True, max_length=20)  # Field name made lowercase.
    visittypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitTypeID')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.
    billmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BillModesID', related_name='staffpayments_billmodesid_set')  # Field name made lowercase.
    staffno = models.ForeignKey(Staff, models.DO_NOTHING, db_column='StaffNo')  # Field name made lowercase.
    voucherstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VoucherStatusID', related_name='staffpayments_voucherstatusid_set')  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID')  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffPayments'


class Staffpaymentsext(models.Model):
    paymentvoucherno = models.OneToOneField(Staffpayments, models.DO_NOTHING, db_column='PaymentVoucherNo', primary_key=True)  # Field name made lowercase.
    approvaldatetime = models.DateTimeField(db_column='ApprovalDateTime', blank=True, null=True)  # Field name made lowercase.
    paymodeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PayModeID', blank=True, null=True)  # Field name made lowercase.
    documentno = models.CharField(db_column='DocumentNo', max_length=20)  # Field name made lowercase.
    currenciesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CurrenciesID', related_name='staffpaymentsext_currenciesid_set', blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=19, decimal_places=4)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4)  # Field name made lowercase.
    amountwords = models.CharField(db_column='AmountWords', max_length=400)  # Field name made lowercase.
    approvalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ApprovalStatusID', related_name='staffpaymentsext_approvalstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffPaymentsEXT'


class Subcounties(models.Model):
    subcountycode = models.CharField(db_column='SubCountyCode', primary_key=True, max_length=20)  # Field name made lowercase.
    subcountyname = models.CharField(db_column='SubCountyName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    countycode = models.ForeignKey(Counties, models.DO_NOTHING, db_column='CountyCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubCounties'
        unique_together = (('subcountyname', 'countycode'),)


class Suppliers(models.Model):
    supplierid = models.IntegerField(db_column='SupplierID')  # Field name made lowercase.
    supplierno = models.CharField(db_column='SupplierNo', primary_key=True, max_length=20)  # Field name made lowercase.
    suppliername = models.CharField(db_column='SupplierName', unique=True, max_length=60, blank=True, null=True)  # Field name made lowercase.
    contactperson = models.CharField(db_column='ContactPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Suppliers'


class Suspiciouslogins(models.Model):
    username = models.CharField(db_column='Username', max_length=20, blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=41, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuspiciousLogins'


class Symptomshistory(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    fever = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Fever', blank=True, null=True)  # Field name made lowercase.
    cough = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Cough', related_name='symptomshistory_cough_set', blank=True, null=True)  # Field name made lowercase.
    coughmorethantwoweeks = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CoughMoreThanTwoWeeks', related_name='symptomshistory_coughmorethantwoweeks_set', blank=True, null=True)  # Field name made lowercase.
    difficultyinbreathing = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DifficultyInBreathing', related_name='symptomshistory_difficultyinbreathing_set', blank=True, null=True)  # Field name made lowercase.
    immunizationdetails = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ImmunizationDetails', related_name='symptomshistory_immunizationdetails_set', blank=True, null=True)  # Field name made lowercase.
    otherhistory = models.CharField(db_column='OtherHistory', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    convulsions = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Convulsions', related_name='symptomshistory_convulsions_set', blank=True, null=True)  # Field name made lowercase.
    alteredconsciousness = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AlteredConsciousness', related_name='symptomshistory_alteredconsciousness_set', blank=True, null=True)  # Field name made lowercase.
    vomiting = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Vomiting', related_name='symptomshistory_vomiting_set', blank=True, null=True)  # Field name made lowercase.
    unabletodrinkbreastfeed = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='UnableToDrinkBreastfeed', related_name='symptomshistory_unabletodrinkbreastfeed_set', blank=True, null=True)  # Field name made lowercase.
    pastmedicalhistory = models.CharField(db_column='PastMedicalHistory', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    diarrhoea = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Diarrhoea', related_name='symptomshistory_diarrhoea_set', blank=True, null=True)  # Field name made lowercase.
    diarrhoealongerthantwoweeks = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DiarrhoeaLongerThanTwoWeeks', related_name='symptomshistory_diarrhoealongerthantwoweeks_set', blank=True, null=True)  # Field name made lowercase.
    blooddiarrhoea = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BloodDiarrhoea', related_name='symptomshistory_blooddiarrhoea_set', blank=True, null=True)  # Field name made lowercase.
    passingteacolouredurine = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PassingTeaColouredUrine', related_name='symptomshistory_passingteacolouredurine_set', blank=True, null=True)  # Field name made lowercase.
    feedinghistory = models.CharField(db_column='FeedingHistory', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    pallor = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Pallor', related_name='symptomshistory_pallor_set', blank=True, null=True)  # Field name made lowercase.
    skinpinchreturn = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SkinPinchReturn', related_name='symptomshistory_skinpinchreturn_set', blank=True, null=True)  # Field name made lowercase.
    severewasting = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SevereWasting', related_name='symptomshistory_severewasting_set', blank=True, null=True)  # Field name made lowercase.
    edema = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Edema', related_name='symptomshistory_edema_set', blank=True, null=True)  # Field name made lowercase.
    sunkeneyes = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='SunkenEyes', related_name='symptomshistory_sunkeneyes_set', blank=True, null=True)  # Field name made lowercase.
    jaundice = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Jaundice', related_name='symptomshistory_jaundice_set', blank=True, null=True)  # Field name made lowercase.
    muac = models.IntegerField(db_column='MUAC', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    deepbreathing = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DeepBreathing', related_name='symptomshistory_deepbreathing_set', blank=True, null=True)  # Field name made lowercase.
    flaringofnostrils = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='FlaringOfNostrils', related_name='symptomshistory_flaringofnostrils_set', blank=True, null=True)  # Field name made lowercase.
    intercostalrecession = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='IntercostalRecession', related_name='symptomshistory_intercostalrecession_set', blank=True, null=True)  # Field name made lowercase.
    subcostalrecession = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='subCostalRecession', related_name='symptomshistory_subcostalrecession_set', blank=True, null=True)  # Field name made lowercase.
    pulse = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Pulse', related_name='symptomshistory_pulse_set', blank=True, null=True)  # Field name made lowercase.
    caprefill = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CapRefill', related_name='symptomshistory_caprefill_set', blank=True, null=True)  # Field name made lowercase.
    airway = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Airway', related_name='symptomshistory_airway_set', blank=True, null=True)  # Field name made lowercase.
    wheezing = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Wheezing', related_name='symptomshistory_wheezing_set', blank=True, null=True)  # Field name made lowercase.
    pleuralrub = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PleuralRub', related_name='symptomshistory_pleuralrub_set', blank=True, null=True)  # Field name made lowercase.
    crackles = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Crackles', related_name='symptomshistory_crackles_set', blank=True, null=True)  # Field name made lowercase.
    unconscious = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Unconscious', related_name='symptomshistory_unconscious_set', blank=True, null=True)  # Field name made lowercase.
    lethargic = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='Lethargic', related_name='symptomshistory_lethargic_set', blank=True, null=True)  # Field name made lowercase.
    unabletositstand = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='UnableToSitStand', related_name='symptomshistory_unabletositstand_set', blank=True, null=True)  # Field name made lowercase.
    bulgingfontanelle = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BulgingFontanelle', related_name='symptomshistory_bulgingfontanelle_set', blank=True, null=True)  # Field name made lowercase.
    stiffneck = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StiffNeck', related_name='symptomshistory_stiffneck_set', blank=True, null=True)  # Field name made lowercase.
    kerningssign = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='KerningsSign', related_name='symptomshistory_kerningssign_set', blank=True, null=True)  # Field name made lowercase.
    isbloodtransfusiondesired = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='IsBloodTransfusionDesired', related_name='symptomshistory_isbloodtransfusiondesired_set', blank=True, null=True)  # Field name made lowercase.
    bloodtransfusionstatereasons = models.CharField(db_column='BloodTransfusionStateReasons', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ifdesiredwasbloodgiven = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='IfDesiredWasBloodGiven', related_name='symptomshistory_ifdesiredwasbloodgiven_set', blank=True, null=True)  # Field name made lowercase.
    ifyesvolume = models.IntegerField(db_column='IfYesVolume', blank=True, null=True)  # Field name made lowercase.
    transfusiondate = models.DateTimeField(db_column='TransfusionDate', blank=True, null=True)  # Field name made lowercase.
    bloodunits = models.IntegerField(db_column='BloodUnits', blank=True, null=True)  # Field name made lowercase.
    bloodtransfusionnotgivenstatereasons = models.CharField(db_column='BloodTransfusionNotGivenStateReasons', max_length=200, blank=True, null=True)  # Field name made lowercase.
    otherformsofsupportivecare = models.CharField(db_column='OtherFormsOfSupportiveCare', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reasonsfordiagnosisofseverecomplicatedmalaria = models.CharField(db_column='ReasonsForDiagnosisOfSevereComplicatedMalaria', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reasonsforadmissionwithpositivemalariatest = models.CharField(db_column='ReasonsForAdmissionWithPositiveMalariaTest', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SymptomsHistory'


class Tbintensifiedcasefinding(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    coughingtwoweeksmoreid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CoughingTwoWeeksMoreID', blank=True, null=True)  # Field name made lowercase.
    persistantfeversid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PersistantFeversID', related_name='tbintensifiedcasefinding_persistantfeversid_set', blank=True, null=True)  # Field name made lowercase.
    noticableweightlossid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='NoticableWeightLossID', related_name='tbintensifiedcasefinding_noticableweightlossid_set', blank=True, null=True)  # Field name made lowercase.
    excessivenightsweatsid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ExcessiveNightSweatsID', related_name='tbintensifiedcasefinding_excessivenightsweatsid_set', blank=True, null=True)  # Field name made lowercase.
    poorweightgainid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PoorWeightGainID', related_name='tbintensifiedcasefinding_poorweightgainid_set', blank=True, null=True)  # Field name made lowercase.
    pulmonarytbchroniccoughcontactid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PulmonaryTBChronicCoughContactID', related_name='tbintensifiedcasefinding_pulmonarytbchroniccoughcontactid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBIntensifiedCaseFinding'


class Templates(models.Model):
    templatename = models.CharField(db_column='TemplateName', primary_key=True, max_length=40)  # Field name made lowercase.
    templatetypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TemplateTypeID', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Templates'


class Testinstruments(models.Model):
    testinstrumentid = models.IntegerField(db_column='TestInstrumentID')  # Field name made lowercase.
    testinstrumentno = models.CharField(db_column='TestInstrumentNo', primary_key=True, max_length=20)  # Field name made lowercase.
    testinstrumentname = models.CharField(db_column='TestInstrumentName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    measurementprocedureid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MeasurementProcedureID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.CharField(db_column='LoginID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    userfullname = models.CharField(db_column='UserFullName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TestInstruments'
        unique_together = (('testinstrumentname', 'measurementprocedureid'),)


class Theatreoperations(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    operationdatetime = models.DateTimeField(db_column='OperationDateTime', blank=True, null=True)  # Field name made lowercase.
    leadsurgeon = models.ForeignKey(Staff, models.DO_NOTHING, db_column='LeadSurgeon', blank=True, null=True)  # Field name made lowercase.
    othersurgeon = models.CharField(db_column='OtherSurgeon', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leadanaesthetist = models.ForeignKey(Staff, models.DO_NOTHING, db_column='LeadAnaesthetist', related_name='theatreoperations_leadanaesthetist_set', blank=True, null=True)  # Field name made lowercase.
    otheranaesthetist = models.CharField(db_column='OtherAnaesthetist', max_length=200, blank=True, null=True)  # Field name made lowercase.
    leadnurse = models.ForeignKey(Staff, models.DO_NOTHING, db_column='LeadNurse', related_name='theatreoperations_leadnurse_set', blank=True, null=True)  # Field name made lowercase.
    othernurse = models.CharField(db_column='OtherNurse', max_length=200, blank=True, null=True)  # Field name made lowercase.
    anaesthesiatype = models.CharField(db_column='AnaesthesiaType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    operationclassid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='OperationClassID', blank=True, null=True)  # Field name made lowercase.
    preoperativediagnosis = models.CharField(db_column='PreoperativeDiagnosis', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    plannedprocedures = models.CharField(db_column='PlannedProcedures', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    report = models.CharField(db_column='Report', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    postoperativeinstructions = models.CharField(db_column='PostoperativeInstructions', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    anesthesiologist = models.ForeignKey(Staff, models.DO_NOTHING, db_column='Anesthesiologist', related_name='theatreoperations_anesthesiologist_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheatreOperations'


class Theatreservices(models.Model):
    theatreid = models.IntegerField(db_column='TheatreID')  # Field name made lowercase.
    theatrecode = models.CharField(db_column='TheatreCode', primary_key=True, max_length=20)  # Field name made lowercase.
    theatrename = models.CharField(db_column='TheatreName', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vatpercentage = models.DecimalField(db_column='VATPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TheatreServices'


class Topologysites(models.Model):
    topographicalno = models.CharField(db_column='TopographicalNo', primary_key=True, max_length=20)  # Field name made lowercase.
    topologysitecodeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TopologySiteCodeID', blank=True, null=True)  # Field name made lowercase.
    topologysitename = models.CharField(db_column='TopologySiteName', max_length=800, blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TopologySites'


class Triage(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='Weight', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='Height', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.CharField(db_column='BloodPressure', max_length=10, blank=True, null=True)  # Field name made lowercase.
    headcircum = models.DecimalField(db_column='HeadCircum', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bodysurfacearea = models.DecimalField(db_column='BodySurfaceArea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    respirationrate = models.SmallIntegerField(db_column='RespirationRate', blank=True, null=True)  # Field name made lowercase.
    oxygensaturation = models.DecimalField(db_column='OxygenSaturation', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.SmallIntegerField(db_column='HeartRate', blank=True, null=True)  # Field name made lowercase.
    triagepriorityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TriagePriorityID', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    muac = models.DecimalField(db_column='MUAC', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bmistatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BMIStatusID', related_name='triage_bmistatusid_set', blank=True, null=True)  # Field name made lowercase.
    muacstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MUACStatusID', related_name='triage_muacstatusid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Triage'


class Verificationext(models.Model):
    visitno = models.CharField(db_column='VisitNo', primary_key=True, max_length=20)  # Field name made lowercase. The composite primary key (VisitNo, FromLocation, ToLocation) found, that is not supported. The first column is selected.
    fromlocation = models.CharField(db_column='FromLocation', max_length=20)  # Field name made lowercase.
    tolocation = models.CharField(db_column='ToLocation', max_length=20)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VerificationExt'
        unique_together = (('visitno', 'fromlocation', 'tolocation'),)


class Villages(models.Model):
    villagecode = models.CharField(db_column='VillageCode', primary_key=True, max_length=20)  # Field name made lowercase.
    villagename = models.CharField(db_column='VillageName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    parishcode = models.ForeignKey(Parishes, models.DO_NOTHING, db_column='ParishCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Villages'
        unique_together = (('villagename', 'parishcode'),)


class Visionassessment(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase. The composite primary key (VisitNo, EyeTestID) found, that is not supported. The first column is selected.
    entryorder = models.IntegerField(db_column='EntryOrder')  # Field name made lowercase.
    eyetestid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EyeTestID')  # Field name made lowercase.
    visualacuityrightid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisualAcuityRightID', related_name='visionassessment_visualacuityrightid_set', blank=True, null=True)  # Field name made lowercase.
    visualacuityrightextid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisualAcuityRightExtID', related_name='visionassessment_visualacuityrightextid_set', blank=True, null=True)  # Field name made lowercase.
    visualacuityleftid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisualAcuityLeftID', related_name='visionassessment_visualacuityleftid_set', blank=True, null=True)  # Field name made lowercase.
    visualacuityleftextid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisualAcuityLeftExtID', related_name='visionassessment_visualacuityleftextid_set', blank=True, null=True)  # Field name made lowercase.
    preferentiallookingrightid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PreferentialLookingRightID', related_name='visionassessment_preferentiallookingrightid_set', blank=True, null=True)  # Field name made lowercase.
    preferentiallookingleftid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='PreferentialLookingLeftID', related_name='visionassessment_preferentiallookingleftid_set', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisionAssessment'
        unique_together = (('visitno', 'eyetestid'),)


class Visitfiles(models.Model):
    visitno = models.OneToOneField('Visits', models.DO_NOTHING, db_column='VisitNo', primary_key=True)  # Field name made lowercase.
    filestatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='FileStatusID', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitFiles'


class Visits(models.Model):
    visitid = models.IntegerField(db_column='VisitID')  # Field name made lowercase.
    visitno = models.CharField(db_column='VisitNo', primary_key=True, max_length=20)  # Field name made lowercase.
    patientno = models.ForeignKey(Patients, models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    visitdate = models.DateTimeField(db_column='VisitDate', blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DoctorSpecialtyID', blank=True, null=True)  # Field name made lowercase.
    staffno = models.ForeignKey(Staff, models.DO_NOTHING, db_column='StaffNo', blank=True, null=True)  # Field name made lowercase.
    visitcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitCategoryID', related_name='visits_visitcategoryid_set', blank=True, null=True)  # Field name made lowercase.
    referredby = models.CharField(db_column='ReferredBy', max_length=40, blank=True, null=True)  # Field name made lowercase.
    servicecode = models.ForeignKey(Services, models.DO_NOTHING, db_column='ServiceCode', blank=True, null=True)  # Field name made lowercase.
    billmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BillModesID', related_name='visits_billmodesid_set', blank=True, null=True)  # Field name made lowercase.
    billno = models.CharField(db_column='BillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    insuranceno = models.CharField(db_column='InsuranceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    associatedbillno = models.ForeignKey(Billcustomers, models.DO_NOTHING, db_column='AssociatedBillNo', blank=True, null=True)  # Field name made lowercase.
    membercardno = models.CharField(db_column='MemberCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mainmembername = models.CharField(db_column='MainMemberName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    claimreferenceno = models.CharField(db_column='ClaimReferenceNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    visitstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitStatusID', related_name='visits_visitstatusid_set', blank=True, null=True)  # Field name made lowercase.
    branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', related_name='visits_branchid_set', blank=True, null=True)  # Field name made lowercase.
    accesscashservices = models.BooleanField(db_column='AccessCashServices', blank=True, null=True)  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked', blank=True, null=True)  # Field name made lowercase.
    fingerprintverified = models.BooleanField(db_column='FingerprintVerified', blank=True, null=True)  # Field name made lowercase.
    copaytypeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CoPayTypeID', related_name='visits_copaytypeid_set', blank=True, null=True)  # Field name made lowercase.
    copaypercent = models.DecimalField(db_column='CoPayPercent', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    copayvalue = models.DecimalField(db_column='CoPayValue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    smartcardapplicable = models.BooleanField(db_column='SmartCardApplicable', blank=True, null=True)  # Field name made lowercase.
    visitspriorityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='VisitsPriorityID', related_name='visits_visitspriorityid_set', blank=True, null=True)  # Field name made lowercase.
    communityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CommunityID', related_name='visits_communityid_set', blank=True, null=True)  # Field name made lowercase.
    loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Visits'


class Updatehistory(models.Model):
    originallogin = models.CharField(db_column='OriginalLogin', max_length=500, blank=True, null=True)  # Field name made lowercase.
    systemuser = models.CharField(db_column='SystemUser', max_length=500, blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'updateHistory'
