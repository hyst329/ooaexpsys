from django.db import models

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=80)


class Medicine(models.Model):
    name = models.CharField(max_length=80)


class Prescription(models.Model):
    disease = models.ForeignKey(Disease)
    medicine = models.ForeignKey(Medicine)
    count = models.IntegerField()
