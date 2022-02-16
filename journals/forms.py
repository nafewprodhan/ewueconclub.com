from django import forms
from .models import JournalReview

class JournalReviewForm(forms.ModelForm):
    class Meta:
        model = JournalReview
        fields = ['body']

        labels = {
            'body': ''
        }

    def __init__(self, *args, **kwargs):
        super(JournalReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-sm', 'rows': '4', 'placeholder': "Add a comment"})

