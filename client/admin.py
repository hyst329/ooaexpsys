from django.contrib import admin
from client.models import *

# Register your models here.
admin.site.register(DoctorSpeciality)
admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(Patient)
admin.site.register(Visit)