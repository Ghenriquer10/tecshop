from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações Pessoais", {"fields": ("nome", "telefone", "endereco")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display = ("email", "nome", "is_staff", "is_active")
    search_fields = ("email", "nome")
    ordering = ("email",)


# Registrar o modelo personalizado sem os campos indesejados
admin.site.register(Usuarios, CustomUserAdmin)
