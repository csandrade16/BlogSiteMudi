from django.contrib import admin
from .models import Cadastro


class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(Cadastro)