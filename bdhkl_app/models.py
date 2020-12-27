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

class Destinations(MyBaseClass):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title





