from django.urls import path
from admin_app import views as AdminAppViews

app_name="admin_app"

urlpatterns = [
    path("", AdminAppViews.AdminHomeView.as_view(), name="home"),
    path("insurance/<int:insurance>", AdminAppViews.AdminInsuranceDetialView.as_view(), name="insurance-details"),
    path("insurance/<int:insurance>/patients/<int:patientid>", AdminAppViews.AdminPatientDetialView.as_view(), name="patient-details")
]