from django import forms
from .models import Notice

class NoticeRichTextForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Notice
        fields = "__all__"