from django.contrib import admin
from django.urls import path, include

from .views import home_redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("usuarios.urls")),
]
