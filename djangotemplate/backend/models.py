from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

# Create your models here.

class UserData(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="userdata")
  year = models.IntegerField(default=2018)
  is_admin = models.BooleanField(default = False)

class CommentModel(models.Model):
  comment = models.TextField(blank = True, default = '')

class ClassTagModel(models.Model):
  name = models.CharField(max_length = 50, blank = True, default = '')

class SchoolTagModel(models.Model):
  name = models.CharField(max_length = 50, blank = True, default = '')

class AreaTagModel(models.Model):
  name = models.CharField(max_length = 50, blank = True, default = '')

class PostModel(models.Model):
  title = models.CharField(max_length = 200, blank = True, default = '')
  description = models.TextField(blank = True, default = '')
  comments = models.ManyToManyField(CommentModel, related_name = "post")
  classTags = models.ManyToManyField(ClassTagModel, related_name = "posts")
  schoolTags = models.ManyToManyField(SchoolTagModel, related_name = "posts")
  areaTags = models.ManyToManyField(AreaTagModel, related_name = "posts")
  author = models.ManyToManyField(UserData, related_name = "posts")
  date_submitted = models.DateTimeField(blank=True, null=True)

class LikeModel(models.Model):
  author = models.ManyToManyField(UserData, related_name = "likes")
  post = models.ManyToManyField(PostModel, related_name = "likes")
  date_submitted = models.DateTimeField(blank=True, null=True)

class DislikeModel(models.Model):
  author = models.ManyToManyField(UserData, related_name = "dislikes")
  post = models.ManyToManyField(PostModel, related_name = "dislikes")
  date_submitted = models.DateTimeField(blank=True, null=True)


