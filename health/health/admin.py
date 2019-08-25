from django.contrib import admin
from health.models import user

admin.register(user)(admin.ModelAdmin)
