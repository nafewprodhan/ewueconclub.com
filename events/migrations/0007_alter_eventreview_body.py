# Generated by Django 3.2.8 on 2021-11-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_rename_project_eventreview_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreview',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]