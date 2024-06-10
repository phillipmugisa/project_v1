# Generated by Django 4.2.10 on 2024-06-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0036_transaction_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sms_enabled', models.BooleanField(default=False)),
                ('email_enabled', models.BooleanField(default=False)),
                ('activation_date', models.DateField(blank=True, null=True, verbose_name='Activated on')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='expires on')),
            ],
        ),
    ]