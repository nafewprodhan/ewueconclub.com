# Generated by Django 3.2.8 on 2022-02-15 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20220201_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='contact_information',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='location',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='request_type',
            field=models.CharField(choices=[('EMERGENCY', 'EMERGENCY'), ('URGENT', 'URGENT'), ('STANDARD', 'STANDARD'), ('GROUP & SAVE', 'GROUP & SAVE')], default='STANDARD', max_length=300),
        ),
        migrations.AddField(
            model_name='message',
            name='unit_bag',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
