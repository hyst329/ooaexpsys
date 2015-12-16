from django.db import models


# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return "[%03d] %s" % (self.id, self.name)


class Medicine(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return "[%03d] %s" % (self.id, self.name)


class Prescription(models.Model):
    disease = models.ForeignKey(Disease)
    medicine = models.ForeignKey(Medicine)
    count = models.IntegerField()

    def __str__(self):
        return "%s, %s : %d" % (self.disease, self.medicine, self.count)
