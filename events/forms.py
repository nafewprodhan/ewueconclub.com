from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms

from .models import EventReview, Event


class ReviewForm(ModelForm):
    class Meta:
        model = EventReview
        fields = ['body']

        labels = {
            'body': ''
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-sm', 'rows': '4', 'placeholder': "Add a comment"})


class EventRichTextForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Event
        fields = "__all__"