from django.db import models
import datetime
from stats.models import *


# Create your models here.


class DoctorSpeciality(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return "[SPEC %03d] %s" % (self.id, self.name)


class Doctor(models.Model):
    name = models.CharField(max_length=80)
    speciality = models.ForeignKey(DoctorSpeciality)

    def __str__(self):
        return "[DOC %03d] %s (%s)" % (self.id, self.name, self.speciality.name)


class Qualification(models.Model):
    speciality = models.ForeignKey(DoctorSpeciality)
    category = models.ForeignKey(DiseaseCategory)

    def __str__(self):
        return "%s, %s" % (self.speciality.name, self.category.name)


class Patient(models.Model):
    name = models.CharField(max_length=80)
    birth_date = models.DateField(default=datetime.date.today)
    gender = models.BooleanField(default=False)

    def __str__(self):
        return "[PAT %03d] %s (%s, born %s)" % (self.id, self.name, "M" if self.gender else "F",
                                                self.birth_date)


class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    visit_date = models.DateTimeField(default=datetime.datetime.now)
    visit_repeat = models.IntegerField(default=1)
    diagnosis = models.ForeignKey(Disease, default=None)

    def __str__(self):
        return "[VIS %03d] Patient %s, Doctor %s: %s (for the %s time)" % \
               (self.id, self.patient.name, self.doctor.name, self.visit_date, self.visit_repeat)
