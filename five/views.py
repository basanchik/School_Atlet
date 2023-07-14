from django.shortcuts import render

from five.models import VacantSeat, EducationalOrganization, SiteInformation


def VakantnyeMesta(request):
    bordaer = {
        "bo": VacantSeat.objects.order_by()[:]
    }
    return render(request, 'main/VakantnyeMesta.html ', bordaer)


def DostupSreda(request):
    s = {
        "Col": EducationalOrganization.objects.order_by()[:]
    }
    return render(request, 'main/DostupSreda.html', s)


def UnitedSotr(request):
    d = {
        "h": SiteInformation.objects.order_by()[:]
    }
    return render(request, 'main/UnitedSotr.html', d)