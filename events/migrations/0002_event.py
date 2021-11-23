# Generated by Django 3.2.8 on 2021-11-06 14:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_moderator_moderator_one'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('title', models.CharField(max_length=1000)),
                ('body', ckeditor.fields.RichTextField()),
                ('banner', models.ImageField(upload_to='event-banner/')),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('reg_dead_line', models.DateTimeField()),
                ('is_reg_open', models.BooleanField(default=False)),
                ('event_satus', models.CharField(choices=[('upcoming', 'upcoming'), ('happening', 'Happening'), ('expired', 'Expired')], default='Expired', max_length=100)),
                ('place', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('event_categorie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.eventcategorie')),
                ('executive_committee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.executivecommittiee')),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.moderator')),
            ],
        ),
    ]