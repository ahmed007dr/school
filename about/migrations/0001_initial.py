# Generated by Django 4.2 on 2024-10-13 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('video_url', models.URLField(blank=True, null=True)),
                ('feature1', models.CharField(max_length=255)),
                ('feature2', models.CharField(max_length=255)),
                ('feature3', models.CharField(max_length=255)),
                ('feature4', models.CharField(max_length=255)),
                ('feature5', models.CharField(max_length=255)),
                ('feature6', models.CharField(max_length=255)),
                ('more_details_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]