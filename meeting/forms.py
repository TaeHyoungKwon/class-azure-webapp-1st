from django import forms
from .models import Post,Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget 




class PostForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ('title','photo','message')
        labels ={
            'title':('제목'),
            'photo':('사진'),

        }


class CommentForm(forms.ModelForm):

     class Meta:
        model = Comment
        fields = ['comment_message']
        labels ={
        'comment_message':('내용'),
        }
