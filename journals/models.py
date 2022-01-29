from django.db import models

from user.models import Profile
import uuid
# Create your models here.

class Journals(models.Model):
    title = models.CharField(max_length=3000)
    all_journals = models.ForeignKey('JournalsCategory', on_delete=models.CASCADE)
    authors = models.ManyToManyField('JournalAuthor')
    abstract = models.TextField()
    pdf_drive_link = models.CharField(max_length=10000)
    keyword = models.ManyToManyField('JournalKeyword')
    view_count = models.PositiveIntegerField(default=0)

    published_timestamp = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class JournalsCategory(models.Model): 
    category = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.category)

class JournalAuthor(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.author)

class JournalKeyword(models.Model):
    keyword = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.keyword