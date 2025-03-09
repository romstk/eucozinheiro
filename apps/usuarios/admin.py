from django.contrib import admin

from apps.usuarios.models import Usuario
# Register your models here.

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ("id", "username", "is_superuser","last_login")


admin.site.register(Usuario, ListandoUsuarios)