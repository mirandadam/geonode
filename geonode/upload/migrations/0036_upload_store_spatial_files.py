# Generated by Django 3.2.12 on 2022-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0035_update_uploadsizelimit_objects'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='store_spatial_files',
            field=models.BooleanField(default=True),
        ),
    ]
