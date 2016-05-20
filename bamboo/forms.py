from django.forms import ModelForm,Textarea,BooleanField,CheckboxInput
from .models import Post,Comment
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _



class PostForm(ModelForm):


    class Meta:
        model = Post
        fields = ('title','photo', 'text',)
        labels ={
        	'title':_('제목'),
        	'text':_('내용'),
            'photo':_('사진'),
        }


class CommentForm(ModelForm):

     anonymous = BooleanField(label='익명하시겠습니까?',widget=CheckboxInput(attrs={'style':'width:50,height:50'}),required=False)

     class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['anonymous','message']
        labels ={
        'anonymous':_('익명하시겠습니까?'), 
        'message':_('내용'),
        }

