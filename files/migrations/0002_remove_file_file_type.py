# Generated by Django 4.0.4 on 2022-06-03 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_type',
        ),
    ]
