from django.db import models
import uuid

# Create your models here.

class Notice(models.Model):

    NOTICE_CATS = (
        ("ALL", 'All'),
        ("GM", "General Members"),
        ("AL", "Alumnus"),
        ("FC", "Faculty")
    )

    notice_to = models.CharField(max_length=200, choices=NOTICE_CATS)

    title = models.CharField(max_length=5000)
    body = models.TextField()

    pblished_timestamp = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.title)