from django.db import models
from django.db.models import Model

TYPES = (
    (0, 'Товар'),
    (1, 'Услуга'),
)


class ProductService(Model):
    class Meta:
        verbose_name = 'Товар или услуга'
        verbose_name_plural = 'Товар или услуги'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    type = models.IntegerField(choices=TYPES, verbose_name='Тип', default=1)

    def __str__(self):
        return self.title


class Company(Model):
    class Meta:
        verbose_name = 'арендатор'
        verbose_name_plural = 'арендаторы'

    name = models.CharField(max_length=255, verbose_name='Имя арендатора')
    link = models.CharField(blank=True, null=True, max_length=255, verbose_name='Сайт')
    description = models.TextField(verbose_name='Описание')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    floor = models.IntegerField(verbose_name='Этаж')
    pavilion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Павильон')
    housing = models.IntegerField(blank=True, null=True, verbose_name='Корпус')
    tags = models.ManyToManyField(ProductService, verbose_name='Товары и услуги')

    def __str__(self):
        return self.name


class Lease(Model):
    class Meta:
        verbose_name = 'аренда'
        verbose_name_plural = 'аренды'

    main_photo = models.ImageField(upload_to='images', default=None, verbose_name='Главное фото')
    square = models.FloatField(verbose_name='Площадь')
    cost = models.IntegerField(verbose_name='Цена')
    floor = models.IntegerField(verbose_name='Этаж')
    housing = models.IntegerField(blank=True, null=True, verbose_name='Корпус')
    function = models.TextField(verbose_name='Назначение')
    show = models.BooleanField(default=False, verbose_name='Показывать?')
    order = models.IntegerField(blank=True, null=True, verbose_name='Порядок')

    def __str__(self):
        return '{}, {}, {}'.format(str(self.square), str(self.floor), str(self.cost))


class Photo(Model):
    photo = models.ImageField(upload_to='images', default=None, verbose_name='Фото')
    lease = models.ForeignKey(Lease, on_delete='CASCADE')
