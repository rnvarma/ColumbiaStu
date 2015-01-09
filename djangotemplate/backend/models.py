from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

class LikeModel(models.Model):
  pass

class DislikeModel(models.Model):
  pass

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
  likes = models.ManyToManyField(LikeModel, related_name = "post")
  dislikes = models.ManyToManyField(DislikeModel, related_name = "post")
  comments = models.ManyToManyField(CommentModel, related_name = "post")
  classTags = models.ManyToManyField(ClassTagModel, related_name = "posts")
  schoolTags = models.ManyToManyField(SchoolTagModel, related_name = "posts")
  areaTags = models.ManyToManyField(AreaTagModel, related_name = "posts")

# overriding the Django User model to allow for custom Users
class MyUserManager(BaseUserManager):
  def create_user(self, email, date_of_birth, password=None):
    """
    Creates and saves a User with the given email, date of
    birth and password.
    """
    if not email:
        raise ValueError('Users must have an email address')

    user = self.model(
      email=MyUserManager.normalize_email(email),
      date_of_birth=date_of_birth,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, date_of_birth, password):
    """
    Creates and saves a superuser with the given email, date of
    birth and password.
    """
    u = self.create_user(username,
                    password=password,
                    date_of_birth=date_of_birth
                )
    u.is_admin = True
    u.save(using=self._db)
    return u

class MyUser(AbstractBaseUser):
  email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
  )
  date_of_birth = models.DateField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)


  objects = MyUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['date_of_birth']

  def get_full_name(self):
    # The user is identified by their email address
    return self.email

  def get_short_name(self):
    # The user is identified by their email address
    return self.email

  def __unicode__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    "Does the user have a specific permission?"
    # Simplest possible answer: Yes, always
    return True

  def has_module_perms(self, app_label):
    "Does the user have permissions to view the app `app_label`?"
    # Simplest possible answer: Yes, always
    return True

  @property
  def is_staff(self):
    "Is the user a member of staff?"
    # Simplest possible answer: All admins are staff
    return self.is_admin






