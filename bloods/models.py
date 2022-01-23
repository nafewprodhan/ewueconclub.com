from django.db import models
from user.models import Profile

import uuid

# Create your models here.

class BloodRequest(models.Model):

    BLOOD_GROUPS = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-")
    )

    REQUEST_TYPES = (
        ("EMERGENCY", "EMERGENCY"),
        ("URGENT", "URGENT"),
        ("STANDARD", "STANDARD"),
        ("GROUP & SAVE", "GROUP & SAVE")
    )

    requested_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    patient_details = models.TextField()
    reason_for_transfusion = models.CharField(max_length=2000)
    blood_group = models.CharField(max_length=50, choices=BLOOD_GROUPS)
    unit_bag = models.PositiveIntegerField(default=1)
    request_type = models.CharField(max_length=300, choices=REQUEST_TYPES)
    location = models.CharField(max_length=1000)
    date_requested = models.DateTimeField()
    contact_info = models.CharField(max_length=2000)
    is_managed = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.requested_by)