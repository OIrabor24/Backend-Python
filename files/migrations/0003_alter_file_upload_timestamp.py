# Generated by Django 4.0.4 on 2022-06-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_file_upload_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
