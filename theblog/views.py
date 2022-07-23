from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView  , CreateView, DetailView
from .models import post
# Create your views here.

class HomeView(ListView):
    model = post
    template_name ='index.html'

class ArticleView(DetailView):
    model = post
    template_name ='article_detail.html'

class AddPostView(CreateView):
    model = post
    template_name = 'add_post.html'
    fields = '__all__'

'''
class Contact(ContactView):
    model = post
    template_name = 'contact.html'
'''
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


