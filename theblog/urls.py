from django.urls import path
from . import views
from .views import  HomeView, ArticleView, AddPostView 

#from .view import ContactView
urlpatterns = [

    path('',HomeView.as_view(), name='index'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>',ArticleView.as_view(), name='article_detail'),

    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('videos/' , views.videos , name='videos'),
    path('gadgets/', views.gadgets, name='gadgets'),
    path('author/' , views.author , name='author'),
    path('single/' , views.single , name='single'),
   # path('$/',views.posts,name='posts')
]