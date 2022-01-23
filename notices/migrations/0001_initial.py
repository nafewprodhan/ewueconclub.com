# Generated by Django 3.2.8 on 2021-11-26 06:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('title', models.CharField(max_length=5000)),
                ('body', models.TextField()),
                ('pblished_timestamp', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
