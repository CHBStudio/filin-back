# Generated by Django 2.0.2 on 2018-02-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_lease_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='productservice',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядок'),
        ),
    ]
