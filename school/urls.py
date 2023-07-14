"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import index, news, docs, newsitem
from base.views import about, sys, obraz
from second.views import ObrazStandart, TrenerSostav
from three.views import MaterialTexOb, Stipendia, PayUslugi
from four.views import Economy
from five.views import VakantnyeMesta, DostupSreda, UnitedSotr


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about', about, name="about"),
    path('news', news, name="news"),
    path('docs', docs, name="docs"),
    path('sys', sys, name="sys"),
    path('obraz', obraz, name="obraz"),
    path('ObrazStandart', ObrazStandart, name="ObrazStandart"),
    path('TrenerSostav', TrenerSostav, name="TrenerSostav"),
    path('MaterialTexOb', MaterialTexOb, name="MaterialTexOb"),
    path('PayUslugi', PayUslugi, name="PayUslugi"),
    path('Stipendia', Stipendia, name="Stipendia"),
    path('<Economy', Economy, name="Economy"),
    path('<VakantnyeMesta', VakantnyeMesta, name="VakantnyeMesta"),
    path('<DostupSreda', DostupSreda, name="DostupSreda"),
    path('<UnitedSotr', UnitedSotr, name="UnitedSotr"),
    path('<int:news_id>/', newsitem, name="newsitem"),

]



