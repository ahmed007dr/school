# Generated by Django 4.2 on 2024-10-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_aboutus_video_url_aboutus_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image_long',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]