from django.urls import path
from .views import dashboard

app_name = "usuarios"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
]
