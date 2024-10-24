# Generated by Django 4.2 on 2024-10-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settingz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('title_logo', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('site_name', models.CharField(max_length=100)),
                ('design_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
