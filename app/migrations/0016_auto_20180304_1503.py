# Generated by Django 2.0.2 on 2018-03-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180304_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядок'),
        ),
    ]
