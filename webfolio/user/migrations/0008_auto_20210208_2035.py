# Generated by Django 3.1.1 on 2021-02-08 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210201_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='title',
        ),
    ]