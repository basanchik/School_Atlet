from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from main.models import News, Document


def index(request):
    news = {
        "news": News.objects.order_by('-date')[:3]
    }
    return render(request, 'main/home.html', news)


def about(request):
    return render(request, 'main/aboutus.html')


def news(request):
    object_list = News.objects.order_by('-date')[:]
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, 'main/news.html',  {'objects': objects})


def docs(request):
    text = {
        "docs": Document.objects.order_by('-dateDocs')[:]

    }
    return render(request, 'main/OurDocs.html', text)


def sys(request):

    return render(request, 'main/OurStruct.html')


def newsitem(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'main/newsform.html', {'news': news})






