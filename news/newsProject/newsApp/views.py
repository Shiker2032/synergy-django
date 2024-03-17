
from django.shortcuts import render
from .models import News


def index(request):
    news = News.objects.all()
    _context = {
        'title': 'Список новостей',
        'news': news
    }
    return render(request, 'index.html', context=_context)