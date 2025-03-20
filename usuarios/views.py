from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(
        request, "usuarios/dashboard.html"
    )  # Criamos um template para a dashboard
