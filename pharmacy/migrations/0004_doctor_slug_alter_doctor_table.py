# Generated by Django 4.2 on 2023-07-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_alter_doctor_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterModelTable(
            name='doctor',
            table='pharmacy_Doctor',
        ),
    ]