# Generated by Django 3.2.8 on 2021-11-20 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_eventreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventreview',
            old_name='project',
            new_name='event',
        ),
    ]
