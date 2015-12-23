from django.db import models
from stats.models import *

# Create your models here.


class Medicine(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return "[MED %03d] %s" % (self.id, self.name)


class Prescription(models.Model):
    disease = models.ForeignKey(Disease)
    medicine = models.ForeignKey(Medicine)
    count = models.IntegerField()

    def __str__(self):
        return "%s, %s : %d" % (self.disease, self.medicine, self.count)
