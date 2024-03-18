from django.urls import path
from admin_app import views as AdminAppViews

app_name="admin_app"

urlpatterns = [
    path("", AdminAppViews.AdminHomeView.as_view(), name="home"),

    path("insurance/<int:insurance_number>/", AdminAppViews.AdminInsuranceDetialView.as_view(), name="insurance-details"),
    path("insurance/<int:insurance_number>/suspend/", AdminAppViews.modifyInsuranceStatusView, name="insurance-suspend"),
    path("insurance/<int:insurance_number>/patient/<int:patientno>/", AdminAppViews.assignPatienttoFamily, name="insurance-assign-patient"),
    path("insurance/<int:insurance_number>/credit/", AdminAppViews.CreditAccountView.as_view(), name="insurance-credit-account"),

    path("patients/<int:patientno>/", AdminAppViews.AdminPatientDetialView.as_view(), name="patient-details"),
    path("patients/<int:patientno>/insurance/", AdminAppViews.AdminPatientInsuranceDetailsView.as_view(), name="patient-insurance-details"),
    path("patients/<int:patientno>/moa", AdminAppViews.PrincipleDocumentView.as_view(), name="principle-documents"),
    path("patients/<int:patientno>/payments/", AdminAppViews.AdminPatientMakePaymentsView.as_view(), name="patient-make-payments"),

    
    path('pdf/<pk>/', AdminAppViews.pdf_view, name='pdf_view'),
]