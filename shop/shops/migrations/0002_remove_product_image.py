# Generated by Django 4.1.7 on 2023-02-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
