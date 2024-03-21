# Generated by Django 5.0.2 on 2024-03-19 12:09

import myauth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=myauth.models.user_images_directory_path),
        ),
        migrations.DeleteModel(
            name='ProfileImages',
        ),
    ]
