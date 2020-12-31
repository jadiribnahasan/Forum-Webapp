from django import forms
from django.contrib.auth.models import User
from .models import Thread, Forum, Post
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


class ThreadCreationForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = [
            'title',
            'discussion',
        ]


class ForumCreationForm(forms.ModelForm):

    class Meta:
        model = Forum
        fields = [
            'name',
            'description',
        ]


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'comment'
        ]
