# Generated by Django 4.2.10 on 2024-06-09 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0037_appsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionservice',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]