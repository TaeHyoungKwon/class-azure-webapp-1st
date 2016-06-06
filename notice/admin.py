from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Post,Comment





class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields='__all__'
        
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title')






@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

