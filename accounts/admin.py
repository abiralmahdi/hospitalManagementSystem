from django.contrib import admin
from .models import*
from django.apps import apps
from django.contrib.auth.admin import UserAdmin

#  Register your models here
app = apps.get_app_config('index')
app2 = apps.get_app_config('accounts')

for model_name, model in app.models.items():
    admin.site.register(model)

for model_name, model in app2.models.items():
    admin.site.register(model)
