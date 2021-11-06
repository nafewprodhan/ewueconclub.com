from django.db import models
from ckeditor.fields import RichTextField
from user.models import Executivecommittiee, Moderator
import uuid

# Create your models here.

class EventCategorie(models.Model):
    title = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

class Event(models.Model):

    event_status_list = (
        ('upcoming', 'upcoming'),
        ('happening', 'Happening'),
        ('expired', 'Expired')
    )

    event_categorie = models.ForeignKey(EventCategorie, on_delete=models.DO_NOTHING)
    moderator = models.ForeignKey(Moderator, on_delete=models.DO_NOTHING)
    executive_committee = models.ForeignKey(Executivecommittiee, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=1000)
    body = RichTextField()
    banner = models.ImageField(upload_to='event-banner/')

    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    reg_dead_line = models.DateTimeField()
    is_reg_open = models.BooleanField(default=False)
    event_satus = models.CharField(max_length=100, choices=event_status_list, default=event_status_list[2][0])

    place = models.CharField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)