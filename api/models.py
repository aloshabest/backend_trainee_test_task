from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    photo = models.JSONField(null=True)