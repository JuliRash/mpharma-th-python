from pyexpat import model
from django.contrib import admin

from api.models import Diagnosis


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('category_code', 'full_description')


admin.site.register(Diagnosis, DiagnosisAdmin)
