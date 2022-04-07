from django.db import models
from django.urls import reverse
# Create your models here.

class picture(models.Model):
    title = models.CharField('Название', max_length=50)
    opisanie = models.CharField('Описание', max_length=50)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural ='Картинки'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})