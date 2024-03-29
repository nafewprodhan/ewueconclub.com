# Generated by Django 3.2.8 on 2021-11-20 04:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_moderator_moderator_one'),
        ('events', '0004_auto_20211119_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventReview',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
