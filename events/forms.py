from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms

from .models import EventReview


class ReviewForm(ModelForm):
    class Meta:
        model = EventReview
        fields = ['body']

        labels = {
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-sm'})