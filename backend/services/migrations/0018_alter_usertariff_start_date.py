# Generated by Django 4.2 on 2024-03-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_alter_tariff_test_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertariff',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
