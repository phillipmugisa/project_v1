from django.urls import path
from admin_app import views as AdminAppViews

app_name="admin_app"

urlpatterns = [
    path("", AdminAppViews.HomeView.as_view(), name="home"),
    path("schemes/", AdminAppViews.SchemeListView.as_view(), name="schemes"),
    path("schemes/<int:insurance_number>", AdminAppViews.SchemeDetailsView.as_view(), name="scheme-details"),
    path("schemes/create", AdminAppViews.SchemeCreateView.as_view(), name="create-scheme"),
]