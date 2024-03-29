from django.db import models
from django.db.models.deletion import DO_NOTHING
from user.models import Profile
import uuid

# Create your models here.

class EblogCategorie(models.Model):
    title = models.CharField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)


class Eblog(models.Model):
    eblog_cats = models.ForeignKey(EblogCategorie, on_delete=models.DO_NOTHING)
    submitted_by = models.ForeignKey(Profile, on_delete=DO_NOTHING, null=True, blank=True)
    blog_authors = models.ManyToManyField('EblogAuthor')
    other_authors_username = models.CharField(max_length=3000, null=True, blank=True)
    title = models.CharField(max_length=3000)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blog-thumbnail/')
    docx_drive_link = models.CharField(max_length=5000, null=True, blank=True)
    eblog_tags = models.ManyToManyField('EblogTag')
    keywords = models.CharField(max_length=5000, null=True, blank=True)
    published_timestamp = models.DateTimeField()
    is_published = models.BooleanField(default=False, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-view_count', '-published_timestamp']


class EblogTag(models.Model):
    name = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)

class EblogReview(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Eblog, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return str(self.blog)

class EblogAuthor(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.author)
