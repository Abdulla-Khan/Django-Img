from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    photos = models.CharField(max_length=20, null=True)
    hour = models.CharField(max_length=20, null=True)
    week = models.CharField(max_length=20, null=True)
    collaborations = models.CharField(max_length=10, null=True)
    profile = models.ImageField(upload_to='profile_pics', null=True)
    feedImage = models.ImageField(blank=True),

    def __str___(self):
        return self.name


class PostFeed(models.Model):
    post = models.ForeignKey(Todo, default=None, on_delete=models.CASCADE)
    feedImage = models.ImageField(upload_to='feed')

    def __str__(self):
        return self.post.name
