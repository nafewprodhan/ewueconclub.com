from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

# from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-md'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'std_alum', 'institution',
                    'department', 'uni_email', 'std_id', 'profile_image',
                    'headline', 'about_yourself', 'blood_group', 'location',
                    'phone_number', 'social_facebook', 'social_linkedin']
        labels = {
            'std_alum': 'I am a/an',
            'std_id': 'University ID',
            'uni_email': 'University email',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-md'})


# class SkillForm(ModelForm):
#     class Meta:
#         model = Skill
#         fields = '__all__'
#         exclude = ['owner']

#     def __init__(self, *args, **kwargs):
#         super(SkillForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})


# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ['name', 'email', 'subject', 'body']

#     def __init__(self, *args, **kwargs):
#         super(MessageForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})
