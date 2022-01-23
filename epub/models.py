from django.db import models

from user.models import Profile
import uuid



# Create your models here.

class Epub(models.Model):
    title = models.CharField(max_length=3000)
    authors = models.ManyToManyField('EpubAuthor')
    abstract = models.TextField()
    pdf_link = models.CharField(max_length=10000)
    keyword = models.CharField(max_length=3000)
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)

    published_timestamp = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
class EpubAuthor(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.author)