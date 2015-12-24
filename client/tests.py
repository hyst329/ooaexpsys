from django.test import TestCase
from client.models import *
import random


# Create your tests here.
class ClientTest(TestCase):
    def test_1(self):
        for i in range(1, 4):
            DoctorSpeciality.objects.create(name="Speciality %s" % i)
        for i in range(1, 11):
            Doctor.objects.create(name="Disease %s" % i, speciality_id=random.randint(1, 3))
        for i in range(1, 51):
            Patient.objects.create(name="Patient %s" % i)
        for i in range(1, 11):
            Disease.objects.create(name="Disease %s" % i, category_id=random.randint(1, 3))
        doc = random.choice(Doctor.objects.all())
        response = self.client.post("/", {"doctors": str(doc.id)})
        self.assertRedirects(response, "/client/doctor/%s" % doc.id, 302, 301)

    def test_2(self):
        for i in range(1, 4):
            DoctorSpeciality.objects.create(name="Speciality %s" % i)
        for i in range(1, 11):
            Doctor.objects.create(name="Disease %s" % i, speciality_id=random.randint(1, 3))
        for i in range(1, 51):
            Patient.objects.create(name="Patient %s" % i)
        for i in range(1, 11):
            Disease.objects.create(name="Disease %s" % i, category_id=random.randint(1, 3))
        doc = random.choice(Doctor.objects.all())
        pat = random.choice(Patient.objects.all())
        dis = random.choice(Disease.objects.all())
        response = self.client.post("/client/doctor/%s/serve" % doc.id, {"patients": pat.id,
                                                                         "diseases": dis.id})
        self.assertRedirects(response, "/expsys/medicines/%s" % dis.id, 301)
