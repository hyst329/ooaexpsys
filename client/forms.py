from django import forms

from client.models import *


class DoctorForm(forms.Form):
    choices = [(d.id, d.name) for d in Doctor.objects.all()]
    doctors = forms.ChoiceField(choices=choices)

class ServeForm(forms.Form):
    pchoices = [(p.id, p.name) for p in Patient.objects.all()]
    patients = forms.ChoiceField(choices=pchoices)
    dchoices = [(d.id, d.name) for d in Disease.objects.all()]
    diseases = forms.ChoiceField(choices=dchoices)

