# Generated by Django 4.0.4 on 2022-05-29 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_remove_majlis_people_alter_majlis_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='majlis',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='majlis',
            name='people',
            field=models.ManyToManyField(related_name='people', to='accounts.profile'),
        ),
    ]
