# Generated by Django 3.2.9 on 2022-11-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_propertise_bathroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='wallet',
        ),
        migrations.RemoveField(
            model_name='propertise',
            name='image',
        ),
        migrations.RemoveField(
            model_name='propertise',
            name='preview1',
        ),
        migrations.RemoveField(
            model_name='propertise',
            name='preview2',
        ),
        migrations.RemoveField(
            model_name='propertise',
            name='preview3',
        ),
        migrations.RemoveField(
            model_name='propertise',
            name='preview4',
        ),
        migrations.CreateModel(
            name='propertiseimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.propertise')),
            ],
        ),
    ]