from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class FindByTag(forms.Form):
    t = forms.SlugField(max_length=80)
