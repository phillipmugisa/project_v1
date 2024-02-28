from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import AccessMixin

class AdminAndAuthenticatedAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("auth_app:signin"))
        if not request.user.account_type == "ADMIN":
            return redirect(reverse("manager:home"))
        return super().dispatch(request, *args, **kwargs)
