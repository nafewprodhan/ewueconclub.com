# Generated by Django 3.2.8 on 2021-11-25 16:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eblogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EblogTag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eblogs.eblog')),
            ],
        ),
    ]
