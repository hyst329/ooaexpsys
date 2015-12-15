from django.shortcuts import render
from django.http import Http404, HttpResponseServerError, HttpResponse
from expsys.models import *


# Index
def index(request):
    return HttpResponse("Expert System greets you. To use it fully, you must use the API.")


# Most popular medicines by disease name.
def medicines(request, disease_id):
    displaynum = 4
    try:
        d = Disease.objects.get(id=disease_id)
        results = Prescription.objects.filter(disease=d, count__gt=0).order_by("-count")[:displaynum]
        return render(request, "medicine.html", {"d": d, "prescr": results})
    except Disease.DoesNotExist:
        raise Http404("Sorry, but the disease with specific ID (%s) was not found." % disease_id)
    pass
