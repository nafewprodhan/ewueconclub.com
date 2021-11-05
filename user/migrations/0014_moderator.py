# Generated by Django 3.2.8 on 2021-11-04 16:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20211104_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('title', models.CharField(max_length=1000)),
                ('ec_start_date', models.DateField()),
                ('ec_current', models.BooleanField(blank=True, default=False, null=True)),
                ('ec_end_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('moderator_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moderator_one', to='user.profile', verbose_name='moderator_one')),
                ('moderator_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderator_three', to='user.profile', verbose_name='moderator_three')),
                ('moderator_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderator_two', to='user.profile', verbose_name='moderator_two')),
            ],
        ),
    ]
