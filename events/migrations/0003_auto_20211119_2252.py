# Generated by Django 3.2.8 on 2021-11-19 16:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_date_time']},
        ),
        migrations.AlterField(
            model_name='event',
            name='event_satus',
            field=models.CharField(choices=[('upcoming', 'upcoming'), ('happening', 'Happening'), ('expired', 'Expired')], default='expired', max_length=100),
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]