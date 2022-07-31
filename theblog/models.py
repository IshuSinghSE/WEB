from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify
#from django.utils.encoding import python_2_unicode_compatible
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


# POSTS #

class post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )

    title    = models.CharField(max_length=200,default='this is my blog', blank=True, null=True)
    author   = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=200,default="coding",blank=True,null=True)
    body     = RichTextField(blank=True,null=True)
    image    = models.ImageField(upload_to="Images_post/",blank=True,null=True)
    snippet  = models.CharField(max_length=300,default='Vivamus non condimentum orci. Pellentesque venenatis nibh sit amet est vehicula lobortis. Cras eget aliquet eros. Nunc lectus elit, suscipit at nunc sed, finibus imperdiet ipsum.')
    publish  = models.DateTimeField(default=timezone.now)
    created  = models.DateField(auto_now_add=True)
    updated  = models.DateField(auto_now=True)
    status   = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    likes    = models.ManyToManyField(User, related_name="blog_post_likes", blank=True)
    slug     = models.SlugField(max_length=200, null=False, unique=True)
    hit_count_generic =  GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager() 


    class Meta:
        ordering = ('-publish',)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.publish)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
     #   return reverse('article_detail', args=str([self.slug]) )
         return reverse('article_detail', kwargs={ "slug":  self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

   
# CATEGORIES #    
class category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
     #   return reverse('article_detail', args=(str(self.id)) )
         return reverse('index')


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


class Comment(models.Model):
    Post = models.ForeignKey(post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return '%s - %s' % (self.Post.title, self.name)

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)

   