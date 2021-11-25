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
    blogger = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    eblog_cats = models.ForeignKey(EblogCategorie, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=3000)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blog-thumbnail/')

    published_timestamp = models.DateTimeField()
    is_published = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    

    def __str__(self):
        return str(self.title)


class EblogTag(models.Model):
    blog = models.ForeignKey(Eblog, on_delete=models.CASCADE)
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

class EblogReviewReplie(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    eblog_review = models.ForeignKey(EblogReview, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.eblog_review)
