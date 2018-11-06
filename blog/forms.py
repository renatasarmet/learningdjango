from django import forms

from .models import Post, Client


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image',)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'adress',)
