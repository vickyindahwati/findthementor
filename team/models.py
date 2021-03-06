from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CAT_TYPE = (
                 ('BACKEND', 'Backend'),
                 ('FRONTEND', 'Frontend'),
                 )

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    email = models.EmailField()
    full_name = models.CharField(max_length=128)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Materi(models.Model):
    name=models.CharField(max_length=128,null=True,blank=True)
    category = models.CharField(max_length=10, choices=CAT_TYPE)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Schedule(models.Model):
    mentor = models.ForeignKey(UserProfile)
    materi = models.ForeignKey(Materi)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return "{} {}".format(self.mentor, self.materi)
# Create your models here.



