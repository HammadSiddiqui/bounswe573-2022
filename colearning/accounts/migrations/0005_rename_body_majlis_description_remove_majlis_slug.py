# Generated by Django 4.0.4 on 2022-05-26 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_majlis_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='majlis',
            old_name='body',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='majlis',
            name='slug',
        ),
    ]
