from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from auth_app import models as AuthAppModels

class AdminSignUpForm(UserCreationForm):
    class Meta:
        model = AuthAppModels.User
        fields = ("username", "first_name", "last_name", "email")


class AdminSignInForm(AuthenticationForm):
    class Meta:
        model = AuthAppModels.User
        fields = ("username",)