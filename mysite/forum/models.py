from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Forum(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=200)
    discussion = RichTextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=10, default="a")
    comment = RichTextField()
    create_date = models.DateTimeField(default=timezone.now)
    creator = creator = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
