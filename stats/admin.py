from django.contrib import admin

# Register your models here.
from stats.models import *

admin.site.register(Disease)
admin.site.register(DiseaseCategory)