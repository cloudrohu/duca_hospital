# Generated by Django 4.2.3 on 2023-07-19 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_hindi_description'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='blog_Post',
        ),
    ]