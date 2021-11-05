# Generated by Django 3.2.8 on 2021-10-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_experience_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('Department of Economics', 'Department of Economics'), ('Department of Business Administration', 'Department of Business Administration')], max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institution',
            field=models.CharField(choices=[('East West University', 'East West University'), ('BRAC University', 'BRAC University'), ('Dhaka University', 'Dhaka University')], max_length=200),
        ),
    ]
