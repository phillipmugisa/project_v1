# django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import login, logout

# custom
from auth_app import forms as AuthAppForms

class SignInView(View):
    template_name="auth_app/sign_in.html"
    context_data={}

    def get(self, request):
        form = AuthAppForms.AdminSignInForm()
        self.context_data["form"] = form
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        form = AuthAppForms.AdminSignInForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse("admin_app:home"))

        self.context_data["form"] = form
        messages.add_message(request, messages.ERROR, _("Invalid Inputs."))
        return render(request, template_name=self.template_name, context=self.context_data)

class SignUpView(View):
    template_name="auth_app/sign_up.html"
    context_data={}

    def get(self, request):
        form = AuthAppForms.AdminSignUpForm()
        self.context_data["form"] = form
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        form = AuthAppForms.AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("auth_app:signin"))

        self.context_data["form"] = form
        messages.add_message(request, messages.ERROR, _("Invalid Inputs."))
        return render(request, template_name=self.template_name, context=self.context_data)


def LogoutView(request):
    logout(request)
    return redirect(reverse("auth_app:signin"))


class ProfileView(View):
    template_name="auth_app/profile.html"
    context_data={}

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse("auth_app:signin"))

        form = AuthAppForms.AdminSignUpForm(instance = request.user)
        self.context_data["form"] = form
        return render(request, template_name=self.template_name, context=self.context_data)
        return render(request, template_name=self.template_name, context=self.context_data)

    def post(self, request):
        form = AuthAppForms.AdminSignUpForm(instance = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("auth_app:logout"))

        self.context_data["form"] = form
        messages.add_message(request, messages.ERROR, _("Invalid Inputs."))
        return render(request, template_name=self.template_name, context=self.context_data)