# Generated by Django 4.2 on 2024-03-27 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_tariff_test_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user_tariff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='services.usertariff', verbose_name='Тариф пользователя'),
        ),
        migrations.AlterField(
            model_name='usertariff',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='usertariff',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начала'),
        ),
    ]
