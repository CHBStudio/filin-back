# Generated by Django 2.0.2 on 2018-02-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_productservice_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images', verbose_name='Фото'),
        ),
    ]
