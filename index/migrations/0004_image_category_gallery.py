# Generated by Django 5.1.1 on 2024-10-14 07:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.image_category')),
            ],
        ),
    ]
