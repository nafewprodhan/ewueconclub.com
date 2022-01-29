from pyexpat import model
from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    replied = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['replied', '-created']