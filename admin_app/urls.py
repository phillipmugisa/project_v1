from django.urls import path
from admin_app import views as AdminAppViews

app_name="admin_app"

urlpatterns = [
    path("", AdminAppViews.HomeView.as_view(), name="home"),
    path("schemes/", AdminAppViews.SchemeListView.as_view(), name="schemes"),
    path("schemes/<int:insurance_number>/", AdminAppViews.SchemeDetailsView.as_view(), name="scheme-details"),
    path("schemes/<int:insurance_number>/delete/", AdminAppViews.SchemeDeleteView.as_view(), name="scheme-delete"),
    path("schemes/<int:insurance_number>/credit/", AdminAppViews.CreditAccountView.as_view(), name="scheme-credit"),
    path("schemes/<int:insurance_number>/edit/", AdminAppViews.EditAccountView.as_view(), name="scheme-edit"),
    path("schemes/<int:insurance_number>/statements/", AdminAppViews.SchemeTransactionStatementView.as_view(), name="scheme-statement"),
    path("schemes/<int:insurance_number>/invoices/", AdminAppViews.SchemeInvoicesView.as_view(), name="scheme-invoices"),
    path("schemes/<int:insurance_number>/invoices/<str:invoiceno>/detail/", AdminAppViews.SchemeInvoiceDetailView.as_view(), name="scheme-invoices-details"),
    path("schemes/create", AdminAppViews.SchemeCreateView.as_view(), name="create-scheme"),
    path("schemes/<int:insurance_number>/patient/<int:patientno>/", AdminAppViews.SchemmePatientView.as_view(), name="scheme-patient"),


    path("patient/<int:patientno>/", AdminAppViews.PatientDetails.as_view(), name="patient-details"),
    path("patient/<int:patientno>/membership/", AdminAppViews.PatientMembershipDetails.as_view(), name="patient-membership"),
    path("patient/<int:patientno>/payment/", AdminAppViews.PatientPaymentView.as_view(), name="patient-payment"),

    path("services/", AdminAppViews.ServicesView.as_view(), name="services"),

    path("pos/", AdminAppViews.POSView.as_view(), name="pos"),
    path("pos/schemes/<int:insurance_number>/patients/", AdminAppViews.POSSchemePatientsView.as_view(), name="pos-scheme-patients"),

    path("pos/services/", AdminAppViews.POSServicesView.as_view(), name="pos-services"),
    path("pos/schemes/", AdminAppViews.POSSchemesView.as_view(), name="pos-schemes"),

    path("transactions/", AdminAppViews.TransactionsView.as_view(), name="transactions"),
]