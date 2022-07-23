from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
# Create your models here.


# CATEGORIES #    
class category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


choices = category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)


# POSTS #
class post(models.Model):
    title    = models.CharField(max_length=200,default='My blog is here.')
    author   = models.ForeignKey(User,on_delete=models.CASCADE, default='1')
    category = models.CharField(max_length=200,choices=choice_list,default="-------",blank=True,null=True)
    body  = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="Images_post/",blank=True,null=True)
    date  =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.date)

    def get_absolute_url(self):
        return reverse('index')#, args=(str(self.id)))