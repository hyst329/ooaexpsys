from django.db import models
import datetime


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


class Patient(models.Model):
    name = models.CharField(max_length=80)
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "[DOC %03d] %s (born %s)" % (self.id, self.name, self.birth_date)


class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    visit_date = models.DateTimeField(default=datetime.datetime.now)
    visit_repeat = models.IntegerField(default=1)

    def __str__(self):
        return "[VIS %03d] Patient %s, Doctor %s: %s (for the %s time)" % \
               (self.id, self.patient.name, self.doctor.name, self.visit_date, self.visit_repeat)
