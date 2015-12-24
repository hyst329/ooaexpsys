from django.shortcuts import render
from django.http import Http404, HttpResponseServerError, HttpResponse, HttpResponseRedirect
from expsys.forms import *


# Index
def expsys_index(request):
    if request.method == 'POST':
        form = ExpsysForm(request.POST)
        if form.is_valid():
            p = request.POST
            if "diseases" in p:
                return HttpResponseRedirect('/expsys/medicine/%s' % p["diseases"])
    else:
        form = ExpsysForm()
        return render(request, "expsys.html", {"form": form})


# After the prescription
def expsys_thanks(request):
    return HttpResponse("Thank you. Your prescription has been added to the database.")


# Most popular medicines by disease name.
def expsys_medicines(request, disease_id):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, disease_id=disease_id)
        if form.is_valid():
            p = request.POST
            if "prescr" in p and "medicines" in p:
                mpid = int(p["prescr"])
                mid = int(p["medicines"])
                medicine_id = mpid if mpid > 0 else mid
                try:
                    pr = Prescription.objects.get(disease=disease_id, medicine=medicine_id)
                    pr.count += 1
                    pr.save()
                except Prescription.DoesNotExist:
                    d = Disease.objects.get(id=disease_id)
                    m = Medicine.objects.get(id=medicine_id)
                    Prescription.objects.create(disease=d, medicine=m, count=1)
            return HttpResponseRedirect('/')
    else:
        try:
            form = PrescriptionForm(disease_id=disease_id)
            return render(request, "medicine.html", {"d": disease_id, "form": form})
        except Disease.DoesNotExist:
            raise Http404("Sorry, but the disease with specific ID (%s) was not found." % disease_id)
        pass
