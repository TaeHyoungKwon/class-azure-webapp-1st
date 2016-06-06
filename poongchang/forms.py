from django import forms
from .models import Post,Comment
from django.forms import ModelForm,Textarea
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ('title','photo','link','message')
        labels ={
            'title':('제목'),
            'link' :('유투브 링크 ID값'),
            'photo':('사진'),

        }



class CommentForm(ModelForm):

     class Meta:
        model = Comment
        fields = ['comment_message']
        labels ={
        'comment_message':('내용'),
        }
