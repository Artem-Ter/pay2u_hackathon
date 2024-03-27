# Generated by Django 4.2 on 2024-03-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_rename_period_tariff_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='duration',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 месяц'), (3, '3 месяца'), (6, '6 месяцев'), (12, '12 месяцев')], verbose_name='Срок'),
        ),
    ]
