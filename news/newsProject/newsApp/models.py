from django.db import models

# Create your models here.

class News(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Картинка')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural='Новости'
        verbose_name='Новость'
        ordering=['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']
        



