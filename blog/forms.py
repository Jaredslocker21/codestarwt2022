from .models import Comment
from django import forms


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
