from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView , CreateView, DetailView, UpdateView, DeleteView
from .models import post, category, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import PostForm, EditForm
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from taggit.models import Tag

from django.contrib import messages
from django.http import JsonResponse
import re
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.conf import settings

import datetime


# Create your views here.


class HomeView(ListView):
    model = post
    template_name = "index.html"
    ordering = ['-publish']
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context.update({'posts': post.objects.filter(approved =True).order_by('-publish',)})
        context.update({'popular': post.objects.filter(approved =True).order_by('-publish','-hit_count_generic__hits')[0:4],})
        context.update({'popular_posts': post.objects.filter(approved =True).order_by('-hit_count_generic__hits')[0:5],})
        context["category_menu"] = category_menu
        return context



class ArticleView(HitCountDetailView):
    model = post
    template_name ='article_detail.html'
    
    #ordering = ['-publish']
    #paginate_by = 1
    count_hit = True

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        #post_list = post.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        context.update({'popular_posts': post.objects.order_by('-hit_count_generic__hits')[:5],})
        #stuff = get_object_or_404(post, id=self.kwargs[slug])
        #total_likes = stuff.total_likes()

        liked = False
        #if stuff.likes.filter(id=self.request.user.id).exists():
         #   liked = True

       # context["total_likes"] = total_likes
        #context["post_list"] = post_list
        context["liked"] = liked
        context["category_menu"] = category_menu
        return context

class AddPostView(CreateView):
    model = post
    template_name = 'add_post.html'
    form_class = PostForm
   
    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context  
    
class UpdatePostView(UpdateView):
    model = post
    form_class = EditForm
    template_name ='update_post.html'
    #fields = ['title','author','category','body','image']

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def CategoryView(request, categories):
    category_posts = post.objects.filter(category=categories.replace('-',' '))
    return render(request, 'categories.html', {'categories':categories.replace('-',' ').title(), 'category_posts':category_posts})

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
 

def CategoryList(request):
    category_list_menu = category.objects.all()
    return render(request, 'categories_list.html',{'category_list_menu':category_list_menu})


def LikeView(request, pk):
    posts = get_object_or_404(post,id=request.POST.get('like_id'))
    liked = False
    if posts.likes.filter(id=request.user.id).exists():
        posts.likes.remove(request.user)
        liked = False
    else:
        posts.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

def index1(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.name = name
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = 'Hello ' + name + ', Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email. checkout our website --- https://ishusinghse.github.io/'
        email_from = 'candyking1002263@gmail.com'#settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)
        # messages.success(request, "Newsletter Sent! ")
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
        # return render(request, 'contact.html')
    return render(request, 'index.html')

def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        res = JsonResponse({'msg': 'Email is required.'})
    elif SubscribedUsers.objects.get(email = email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html') 

def reviews(request):
    return render(request,'reviews.html') 

def videos(request):
    return render(request,'videos.html') 

def gadgets(request):
    return render(request,'gadgets.html') 

def author(request):
    return render(request,'author.html') 

def single(request):
    return render(request,'single.html') 


