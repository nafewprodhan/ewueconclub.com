# Generated by Django 3.2.8 on 2021-12-01 03:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0019_alter_moderator_moderator_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('patient_details', models.TextField()),
                ('reason_for_transfusion', models.CharField(max_length=2000)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=50)),
                ('unit_bag', models.PositiveIntegerField(default=1)),
                ('request_type', models.CharField(choices=[('EMERGENCY', 'EMERGENCY'), ('URGENT', 'URGENT'), ('STANDARD', 'STANDARD'), ('GROUP & SAVE', 'GROUP & SAVE')], max_length=300)),
                ('location', models.CharField(max_length=1000)),
                ('date_requested', models.DateTimeField()),
                ('contact_info', models.CharField(max_length=2000)),
                ('is_managed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
