from django.contrib import admin
from .models import PhoneModel
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(PhoneModel)
admin.site.unregister(Group)