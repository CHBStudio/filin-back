# Generated by Django 2.0.2 on 2018-02-28 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180228_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productservice',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images', verbose_name='Иконка'),
        ),
    ]
