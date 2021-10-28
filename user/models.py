from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):

    st_al_list = (
        ('student', 'Student'),
        ('Alumnus', 'Alumnus'),
    )

    institution_list = (
        ('EWU', 'East West University'),
        ('BRAC', 'BRAC University'),
        ('DU', 'Dhaka University'),
    )

    department_list = (
        ('ECO', 'Department of Economics'),
        ('BBA', 'Department of Business Administration'),
    )

    blood_group_list = (
        ('A+', 'A+'),
        ('A-', 'A-'),
    )

    location_list = (
        ('banasree', 'Banasree'),
        ('aftabnagar', 'Aftabnagar'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    faculty = models.BooleanField(default=False)
    std_alum = models.CharField(max_length=200, choices=st_al_list)
    institution = models.CharField(max_length=200, choices=institution_list)
    department = models.CharField(max_length=200, choices=department_list)
    uni_email = models.EmailField(max_length=200, unique=True, blank=True, null=True)
    std_id = models.CharField(max_length=20, blank=True, null=True, unique=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    headline = models.CharField(max_length=200, blank=True, null=True)
    about_yourself = models.TextField(blank=True, null=True)
    blood_group = models.CharField(max_length=200, choices=blood_group_list)
    location = models.CharField(max_length=200, choices=location_list)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
