# Generated by Django 2.0.2 on 2018-03-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180303_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='pavilion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Павильон'),
        ),
    ]
