from django.test import TestCase
from stats.models import *
from expsys.models import *
import random


# Create your tests here.
class ExpsysTest(TestCase):
    def test_1(self):
        for i in range(1, 4):
            DiseaseCategory.objects.create(name="Category %s" % i)
        for i in range(1, 11):
            Disease.objects.create(name="Disease %s" % i, category_id=random.randint(1, 3))
        d = random.choice(Disease.objects.all())
        response = self.client.post("/expsys", {"diseases": str(d.id)})
        self.assertRedirects(response, "/expsys/medicine/%s" % d.id, 302, 301)

    def test_2(self):
        for i in range(1, 4):
            DiseaseCategory.objects.create(name="Category %s" % i)
        for i in range(1, 11):
            Disease.objects.create(name="Disease %s" % i, category_id=random.randint(1, 4))
        for i in range(1, 31):
            Medicine.objects.create(name="Medicine %s" % i)
        for i in range(40):
            Prescription.objects.create(disease_id=random.randint(1, 10),
                                        medicine_id=random.randint(1, 30),
                                        count=random.randint(1, 100))
        d = random.choice(Disease.objects.all())
        m = random.choice(Medicine.objects.all())
        ct = Prescription.objects.filter(disease=d, medicine=m)[0] \
            if Prescription.objects.filter(disease=d, medicine=m).exists() else 0
        response = self.client.post("/expsys/medicine/%s" % d.id, {"medicines": str(m.id),
                                                                   "prescr": "-1"})
        self.assertRedirects(response, "/", 301)
        nct = Prescription.objects.filter(disease=d, medicine=m)[0] \
            if Prescription.objects.filter(disease=d, medicine=m).exists() else 0
        self.assertEqual(nct, ct + 1)
