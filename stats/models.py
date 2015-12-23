from django.db import models
import datetime

# Create your models here.


class DiseaseCategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return "[CAT %03d] %s" % (self.id, self.name)


class Disease(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(DiseaseCategory)

    def __str__(self):
        return "[DIS %03d] %s (%s)" % (self.id, self.name, self.category.name)





