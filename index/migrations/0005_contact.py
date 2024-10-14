# Generated by Django 5.1.1 on 2024-10-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_image_category_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
