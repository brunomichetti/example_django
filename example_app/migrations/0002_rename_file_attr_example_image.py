# Generated by Django 3.2 on 2022-06-23 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='example',
            old_name='file_attr',
            new_name='image',
        ),
    ]