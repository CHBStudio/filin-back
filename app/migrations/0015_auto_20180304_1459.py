# Generated by Django 2.0.2 on 2018-03-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20180303_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='function',
            field=models.TextField(blank=True, null=True, verbose_name='Назначение'),
        ),
        migrations.AlterField(
            model_name='lease',
            name='order',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Порядок'),
        ),
    ]
