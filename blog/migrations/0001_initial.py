# Generated by Django 4.2 on 2024-10-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date_posted', models.DateField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]