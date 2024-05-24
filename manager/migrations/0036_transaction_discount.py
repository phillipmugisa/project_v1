# Generated by Django 4.2.10 on 2024-05-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0035_transaction_patient_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Discount'),
        ),
    ]