from django.shortcuts import render

from base.models import About, Sotrudnik, Otdel, Obraz, elementsObraz


def about(request):
    about = {
        "about": About.objects.order_by()[:]
    }
    return render(request, 'main/aboutus.html', about)


def sys(request):
    Sys = {
        "Col": Sotrudnik.objects.order_by()[:],
        "otdels": Otdel.objects.order_by()[:]
    }
    return render(request, 'main/OurStruct.html', Sys)


def obraz(request):
    obrazEl = {
        "elementsObraz": elementsObraz.objects.order_by()[:],
        "nameObraz": Obraz.objects.order_by()[:]
    }
    return render(request, 'main/Obraz.html', obrazEl)