
from django.shortcuts import render
from .models import News, Category


def index(request):
    news = News.objects.all()
    _context = {
        'title': 'Список новостей',
        'news': news,
       
    }
    return render(request, 'index.html', context=_context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.filter(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request,'category.html', context=context)