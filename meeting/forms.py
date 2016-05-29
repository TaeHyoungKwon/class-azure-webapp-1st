from django import forms
from .models import Post,Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','photo','message')
        labels ={
        	'title':('제목'),
        	'photo':('사진'),
            'message':('내용'),
        }       



class CommentForm(forms.ModelForm):

     class Meta:
        model = Comment
        fields = ['comment_message']
        labels ={
        'comment_message':('내용'),
        }
