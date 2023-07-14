from django.shortcuts import render

from three.models import PaidEducationService, Support, EducationalResources


def MaterialTexOb(request):
    Material = {
        'mat': EducationalResources.objects.order_by()[:]
    }
    return render(request, 'main/MaterialTexOb.html', Material)


def Stipendia(request):
    money = {
        'mon': Support.objects.order_by()[:]
    }
    return render(request, 'main/Stipendia.html', money)


def PayUslugi(request):
    pay = {
        'pa': PaidEducationService.objects.order_by()[:]
    }
    return render(request, 'main/PayUslugi.html', pay )



