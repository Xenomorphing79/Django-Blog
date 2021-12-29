from django import forms
from django.forms import widgets
from posts.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'draft',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)