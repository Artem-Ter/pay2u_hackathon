# Generated by Django 4.2 on 2024-03-29 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_remove_tariff_duration_tariff_period_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date'], 'verbose_name': 'Оплата', 'verbose_name_plural': 'Платежи'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='cashback',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Кешбэк'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user_tariff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='services.usertariff', verbose_name='Тариф пользователя'),
        ),
    ]