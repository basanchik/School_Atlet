from django.shortcuts import render
from second.models import FedStandart, PedagogicalStaff

def ObrazStandart(request):
    fedtandart = {
        "fedtandart": FedStandart.objects.order_by()[:]
    }
    return render(request, 'main/ObrazStandart.html', fedtandart)


def TrenerSostav(request):
    trener = {
        "Pedagog": PedagogicalStaff.objects.order_by()[:],
    }
    return render(request, 'main/TrenerSostav.html', trener)

