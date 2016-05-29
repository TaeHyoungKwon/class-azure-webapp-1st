from django import forms
from .models import Comment
from django.forms import ModelForm




class CommentForm(ModelForm):
	class Meta:
	    model = Comment
	    fields = ['message']
	    labels ={
	    'message':('내용'),
	    }
       

