from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):

    st_al_list = (
        ('Student', 'Student'),
        ('Alumni', 'Alumni'),
    )

    institution_list = (
        ('East West University', 'East West University'),
        ('BRAC University', 'BRAC University'),
        ('Dhaka University', 'Dhaka University'),
    )

    department_list = (
        ('Department of Economics', 'Department of Economics'),
        ('Department of Business Administration', 'Department of Business Administration'),
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
    id_verification = models.ImageField(
        null=True, blank=True, upload_to='profile-id-verification/')
    verified = models.BooleanField(default=False)
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
        ordering = ['verified', '-created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Experience(models.Model):

    present_choice = (
        ('y', 'Yes'),
        ('n', 'No')
    )

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    headline = models.CharField(max_length=200)
    company_name = models.CharField( max_length=300)
    start_date = models.DateField()
    present = models.CharField(max_length=200, choices=present_choice, default=present_choice[1][0])
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(max_length= 1000 ,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.company_name)

class Education(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    field_of_study = models.CharField(max_length=200, null=True, blank=True)
    grade = models.CharField(max_length=200, blank=True, null=True) 
    description = models.TextField(max_length= 1000 ,null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.school)

class Executivecommittiee(models.Model):
    title = models.CharField(max_length=1000)

    president = models.ForeignKey(Profile, related_name="president", verbose_name="President", on_delete=models.CASCADE)
    vice_president = models.ForeignKey(Profile, related_name="vice_president", verbose_name="Vice President", on_delete=models.DO_NOTHING)
    general_secretary = models.ForeignKey(Profile, related_name="general_secretary", verbose_name="General Secretary", on_delete=models.DO_NOTHING)
    joint_secretary = models.ForeignKey(Profile, related_name="joint_secretary", verbose_name="Joint Secretary", on_delete=models.DO_NOTHING)    
    treasurer = models.ForeignKey(Profile, related_name="treasurer", verbose_name="Treasurer", on_delete=models.DO_NOTHING)
    event_coordinator = models.ForeignKey(Profile, related_name="event_coordinator", verbose_name="Event Coordinator", on_delete=models.DO_NOTHING)
    head_of_logistics = models.ForeignKey(Profile, related_name="head_of_logistics", verbose_name="Head of Logistics", on_delete=models.DO_NOTHING)

    ec_start_date = models.DateField()
    ec_current = models.BooleanField(default=False, null=True, blank=True)
    ec_end_date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)


class Moderator(models.Model):
    title = models.CharField(max_length=1000)

    moderator_one = models.ForeignKey(Profile, related_name="moderator_one", verbose_name="moderator_one", null=True, blank=True, on_delete=models.DO_NOTHING)
    moderator_two = models.ForeignKey(Profile, related_name="moderator_two", verbose_name="moderator_two", null=True, blank=True, on_delete=models.DO_NOTHING)
    moderator_three = models.ForeignKey(Profile, related_name="moderator_three", verbose_name="moderator_three", null=True, blank=True, on_delete=models.DO_NOTHING)

    ec_start_date = models.DateField()
    ec_current = models.BooleanField(default=False, null=True, blank=True)
    ec_end_date = models.DateField(null=True, blank=True)

    mod_check = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)