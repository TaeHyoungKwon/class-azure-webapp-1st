from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

     class Meta:
        model = Comment
        fields = ['comment_message']
        labels ={
        'comment_message':('내용'),
        }
