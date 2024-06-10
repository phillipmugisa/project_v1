from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import AccessMixin
from manager import models as ManagerModels
from django.utils import timezone

class AdminAndAuthenticatedAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("auth_app:signin"))
        if not request.user.account_type == "ADMIN":
            return redirect(reverse("manager:home"))
        return super().dispatch(request, *args, **kwargs)

class SubscriptionActiveMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        app_settings = ManagerModels.AppSettings.objects.all()
        if not app_settings:
            return redirect(reverse("admin_app:invalid-subscription"))

        if timezone.now().date() > app_settings.first().expiration_date:
            return redirect(reverse("admin_app:invalid-subscription"))
        
        return super().dispatch(request, *args, **kwargs)