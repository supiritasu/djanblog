# Generated by Django 4.2.7 on 2023-11-27 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_rename_commnt_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.timezone, upload_to=''),
        ),
    ]
