# Generated by Django 3.2.15 on 2022-09-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
