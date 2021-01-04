from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MyBaseClass(models.Model):
    title = models.CharField(max_length = 100)
    featured_image = models.ImageField(upload_to='post/')
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(MyBaseClass):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering = ['date_posted']
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class Destinations(MyBaseClass):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length = 200, null = True, blank= True)
    taken_by =  models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['img','caption','taken_by']


    def __str__(self):
        return self.caption






