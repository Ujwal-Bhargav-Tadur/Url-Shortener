# Generated by Django 4.2.1 on 2023-05-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_url_delete_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.URLField(max_length=2000, unique=True),
        ),
    ]
