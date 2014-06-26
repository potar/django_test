from django.contrib import admin

from .models import dynamic_models

# Register your models here.
admin.site.register(dynamic_models.values())
