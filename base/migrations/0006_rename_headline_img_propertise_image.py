# Generated by Django 3.2.9 on 2022-11-22 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_propertise_headline_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertise',
            old_name='headline_img',
            new_name='image',
        ),
    ]
