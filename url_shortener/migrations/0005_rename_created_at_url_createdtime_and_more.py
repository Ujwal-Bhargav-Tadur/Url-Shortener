# Generated by Django 4.2.1 on 2023-05-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0004_alter_url_original_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='created_at',
            new_name='createdTime',
        ),
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
