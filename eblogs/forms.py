from django import forms
from .models import Eblog, EblogReview

class EblogAdminForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Eblog
        fields = "__all__"


class EblogReviewForm(forms.ModelForm):
    class Meta:
        model = EblogReview
        fields = ['body']

        labels = {
            'body': 'Add a comment'
        }

    def __init__(self, *args, **kwargs):
        super(EblogReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-sm', 'rows': '4', 'placeholder': "Add a comment"})


# class EblogReviewRepliesForm(forms.ModelForm):
#     class Meta:
#         model = EblogReviewReplie
#         fields = ['body']

#         labels = {
#             'body': 'Add a reply'
#         }

#     def __init__(self, *args, **kwargs):
#         super(EblogReviewRepliesForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control form-control-sm'})