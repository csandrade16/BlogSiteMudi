from django.contrib import admin
from .models import Publicacao


class PublicaoAdmin(admin.ModelAdmin):
    admin.site.register(Publicacao),
