from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime
# Create your models here.


#profile
class profile(models.Model):
     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
     profile_pic = models.ImageField(blank=True,null=True,upload_to="Images/profile")
     bio = models.TextField()
     facebook_url   = models.URLField(max_length=200,blank=True, null=True )
     instagram_url  = models.URLField(max_length=200,blank=True, null=True )
     twitter_url    = models.URLField(max_length=200,blank=True, null=True )
     pinterest_url  = models.URLField(max_length=200,blank=True, null=True )
     youtube_url    = models.URLField(max_length=200,blank=True, null=True )
     website_url    = models.URLField(max_length=200,blank=True, null=True )
     
     def __str__(self):
       return str(self.user)

     def get_absolute_url(self):
        return reverse('index')

# POSTS #
class post(models.Model):
    title    = models.CharField(max_length=200,default='this is my blog ')
    author   = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=200,default="coding",blank=True,null=True)
    body     = RichTextField(blank=True,null=True)
    image    = models.ImageField(upload_to="Images_post/",blank=True,null=True)
    snippet  = models.CharField(max_length=300,default='Vivamus non condimentum orci. Pellentesque venenatis nibh sit amet est vehicula lobortis. Cras eget aliquet eros. Nunc lectus elit, suscipit at nunc sed, finibus imperdiet ipsum.')
    date     = models.DateField(auto_now_add=True)
    likes    = models.ManyToManyField(User, related_name="blog_post_likes")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.date)

    def get_absolute_url(self):
     #   return reverse('article_detail', args=(str(self.id)) )
         return reverse('index')
   

# CATEGORIES #    
class category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
     #   return reverse('article_detail', args=(str(self.id)) )
         return reverse('index')
