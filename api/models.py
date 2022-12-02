from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    images = models.JSONField(null=True)


