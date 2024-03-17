from django.contrib import admin
from .models import News, Category

# Register your models here.
class NewsAdmin (admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'content', 'created_at', 'photo', 'is_published']
    list_display_links = ['id']
    list_editable = ['category', 'title', 'is_published']
    search_fields = ['title', 'content']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    list_display_links=['title']

    search_fields = ['title']

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin )


