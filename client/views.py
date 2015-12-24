from django.http import HttpResponseRedirect
from django.shortcuts import render
from client.forms import *


# Create your views here.
def client_index(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            p = request.POST
            if "doctors" in p:
                return HttpResponseRedirect('/client/doctor/%s' % p["doctors"])
    else:
        form = DoctorForm()
        return render(request, "doctor.html", {"form": form})


def client_doctors(request, doctor_id):
    visits = Visit.objects.filter(doctor_id=doctor_id, visit_date=datetime.date.today())
    return render(request, "doctorid.html", {"doc": Doctor.objects.get(id=doctor_id),
                                             "visits": visits, "today": datetime.date.today()})


def client_serve(request, doctor_id):
    if request.method == 'POST':
        form = ServeForm(request.POST)
        if form.is_valid():
            p = request.POST
            patient = Patient.objects.get(id=int(p["patients"]))
            disease = Disease.objects.get(id=int(p["diseases"]))
            category = disease.category
            visit = 1
            if Visit.objects.filter(patient=patient, diagnosis__category=category).exists():
                v = Visit.objects.filter(patient=patient, diagnosis__category=category)[0]
                if (datetime.datetime.now() - v.visit_date).days <= 14:
                    visit += v.visit_repeat

            Visit.objects.create(diagnosis=disease, patient=patient, doctor_id=doctor_id, visit_repeat=visit)
            if "diseases" in p:
                return HttpResponseRedirect('/expsys/medicine/%s' % p["diseases"])
    else:
        form = ServeForm()
        return render(request, "doctor.html", {"form": form})
