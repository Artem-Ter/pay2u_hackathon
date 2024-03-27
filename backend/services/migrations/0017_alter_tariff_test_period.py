# Generated by Django 4.2 on 2024-03-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_rename_duration_tariff_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='test_period',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 месяц'), (3, '3 месяца'), (6, '6 месяцев'), (12, '12 месяцев')], null=True, verbose_name='Пробный период'),
        ),
    ]
