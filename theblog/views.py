from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , CreateView, DetailView, UpdateView, DeleteView
from .models import post, category
from django.urls import reverse_lazy
from .forms import PostForm, EditForm
# Create your views here.

class HomeView(ListView):
    model = post
    template_name ='index.html'
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class ArticleView(DetailView):
    model = post
    template_name ='article_detail.html'

class AddPostView(CreateView):
    model = post
    template_name = 'add_post.html'
    form_class = PostForm
    

class UpdatePostView(UpdateView):
    model = post
    form_class = EditForm
    template_name ='update_post.html'
    #fields = ['title','author','category','body','image']

class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

def CategoryView(request, categories):
    category_posts = post.objects.filter(category=categories.replace('-',' '))
    return render(request, 'categories.html', {'categories':categories.replace('-',' ').title(), 'category_posts':category_posts})

   


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


