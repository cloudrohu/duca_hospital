# Generated by Django 4.2 on 2023-07-20 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_service_hindi_name_service_sort_description'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='service',
            table='app_Service',
        ),
    ]