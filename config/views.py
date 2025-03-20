from django.shortcuts import redirect


def home_redirect(request):
    if request.user.is_authenticated:
        return redirect("usuarios:dashboard")
    return redirect("account_login")
