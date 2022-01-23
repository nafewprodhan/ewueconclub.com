from django.db import models
from user.models import Executivecommittiee, Moderator
import uuid

from user.models import Profile

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
    body = models.TextField()
    banner = models.ImageField(upload_to='event-banner/')

    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    reg_dead_line = models.DateTimeField(null=True, blank=True)
    reg_opt = models.BooleanField(default=True, null=True, blank=True)
    is_reg_open = models.BooleanField(default=False)
    event_satus = models.CharField(max_length=100, choices=event_status_list, default=event_status_list[2][0])

    place = models.CharField(max_length=1000)
    tags = models.ManyToManyField('EventTag', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-start_date_time']


class EventTag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class EventReview(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return str(self.event)