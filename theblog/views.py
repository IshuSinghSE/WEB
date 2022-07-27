from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView , CreateView, DetailView, UpdateView, DeleteView
from .models import post, category
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import PostForm, EditForm

# Create your views here.


class HomeView(ListView):
    model = post
    template_name ='index.html'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context



class ArticleView(DetailView):
    model = post
    template_name ='article_detail.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        context["category_menu"] = category_menu
        return context


class AddPostView(CreateView):
    model = post
    template_name = 'add_post.html'
    form_class = PostForm
   
    
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


