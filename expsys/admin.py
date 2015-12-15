from django.contrib import admin

# Register your models here.
from expsys.models import *

admin.site.register(Disease)
admin.site.register(Medicine)
admin.site.register(Prescription)