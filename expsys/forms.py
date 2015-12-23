from django import forms

from expsys.models import *
from stats.models import *


class ExpsysForm(forms.Form):
    choices = [(d.id, d.name) for d in Disease.objects.all()]
    diseases = forms.ChoiceField(choices=choices)


class PrescriptionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        disease_id = kwargs.pop('disease_id', 0)
        super().__init__(*args, **kwargs)
        d = Disease.objects.get(id=disease_id)
        results = Prescription.objects.filter(disease=d, count__gt=0).order_by("-count")[:4]
        results = [(r.medicine.id, "%s (%s prescriptions)" % (r.medicine.name, r.count))
                   for r in results]
        results.append((-1, "Other"))
        self.fields["prescr"].choices = results
        self.fields["medicines"].choices = [(m.id, m.name) for m in Medicine.objects.all()]

    prescr = forms.ChoiceField(widget=forms.RadioSelect())
    medicines = forms.ChoiceField()
