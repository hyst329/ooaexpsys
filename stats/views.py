from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from client.models import *


def stats_bycat(request):
    year = datetime.date.today().year
    vis1 = Visit.objects.filter(visit_date__year=year).values('diagnosis'). \
        annotate(ct=Count('diagnosis'))
    vis2 = Visit.objects.filter(visit_date__year=year - 1).values('diagnosis'). \
        annotate(ct=Count('diagnosis'))
    vis3 = Visit.objects.filter(visit_date__year=year - 2).values('diagnosis'). \
        annotate(ct=Count('diagnosis'))
    vis1total = sum(v["ct"] for v in vis1)
    vis2total = sum(v["ct"] for v in vis2)
    vis3total = sum(v["ct"] for v in vis3)
    data = []
    for d in Disease.objects.all():
        dt = [d.id, d.name]
        for visx in ((vis1, vis1total), (vis2, vis2total), (vis3, vis3total)):
            ct = 0
            for v in visx[0]:
                if v["diagnosis"] == d.id:
                    ct = v["ct"]
            dt.append(ct)
            dt.append(ct * 100 / visx[1] if visx[1] else 0.0)
        data.append(dt)
    return render(request, "statsc.html", {"data": data, "year": year})


def stats_byspec(request):
    year = datetime.date.today().year
    vis1 = Visit.objects.filter(visit_date__year=year).values('doctor'). \
        annotate(ct=Count('doctor'))
    vis2 = Visit.objects.filter(visit_date__year=year - 1).values('doctor'). \
        annotate(ct=Count('doctor'))
    vis3 = Visit.objects.filter(visit_date__year=year - 2).values('doctor'). \
        annotate(ct=Count('doctor'))
    data = []
    for d in Doctor.objects.all():
        dt = [d.id, d.name]
        for visx in (vis1, vis2, vis3):
            ct = 0
            for v in visx:
                if v["doctor"] == d.id:
                    ct = v["ct"]
            dt.append(ct)
        data.append(dt)
    return render(request, "statss.html", {"data": data, "year": year})


def stats_bygenderage(request):
    pass
