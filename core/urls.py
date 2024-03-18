from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from admin_app.views import VerifyFamilyMemberView, DeclineFamilyMemberView

urlpatterns = [
    path("clinic/", include("clinicMas.urls", namespace="clinicMas")),
    path("auth/", include("auth_app.urls", namespace="auth_app")),
    path("", include("admin_app.urls", namespace="admin_app")),
    path('admin/', admin.site.urls),
    
    # path("verify/<uidb64>/", VerifyFamilyMemberView, name="activate_family_member"),
    # path("decline/<uidb64>/", DeclineFamilyMemberView, name="decline_family_member"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)