from django.contrib import admin
from .models import Usuarios


class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "email",
        "data_nascimento",
        "cpf",
        "telefone",
        "endereco",
    )
    search_fields = ("nome", "email", "cpf")
    ordering = ("nome",)


admin.site.register(Usuarios, UsuariosAdmin)
