# Generated by Django 3.2.8 on 2021-12-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eblogs', '0004_auto_20211214_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='eblog',
            name='eblog_tags',
            field=models.ManyToManyField(to='eblogs.EblogTag'),
        ),
    ]
