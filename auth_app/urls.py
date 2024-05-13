from django.urls import path
from auth_app import views as AuthAppViews

app_name = "auth_app"

urlpatterns = [
    path("signin/", AuthAppViews.SignInView.as_view(), name="signin"),
    path("signup/", AuthAppViews.SignUpView.as_view(), name="signup"),
    path("logout/", AuthAppViews.LogoutView, name="logout"),
    path("profile/", AuthAppViews.ProfileView.as_view(), name="profile"),
]