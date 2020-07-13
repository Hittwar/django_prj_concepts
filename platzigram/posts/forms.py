""" Post forms """

# Django
from django import forms

from posts.models import Post

class PostForm(forms.ModelForm):
    """Form Settings"""

    class Meta:
        """Form Settings"""
        model = Post
        fields=('user', 'profile', 'title', 'photo')