from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("clinicMas.urls", namespace="clinicMas")),
    path("auth/", include("auth_app.urls", namespace="auth_app")),
    path("admin/", include("admin_app.urls", namespace="admin_app")),
    path('django/admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)