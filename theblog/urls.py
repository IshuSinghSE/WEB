from django.urls import path, include
from . import views
from .views import  HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView, CategoryList, index1, validate_email

#app_name = 'theblog'


urlpatterns = [

    path('',HomeView.as_view(), name='index'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace ='hitcount')),
    path('newsletter/', views.index1, name='index1'),
    path('validate/', views.validate_email, name='validate_email'),

    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('<slug:slug>',ArticleView.as_view(), name='article_detail'),#path('article/<slug:slug>',ArticleView.as_view(), name='article_detail'),
    
    

    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
    path('category/<str:categories>/',CategoryView, name='category'),
    path('category-list/',CategoryList, name='category_list'),
    #path('like/<slug:slug>',LikeView,name="post_likes"), 
    path('like/<int:pk>',LikeView,name="post_likes"),


    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('videos/' , views.videos , name='videos'),
    path('gadgets/', views.gadgets, name='gadgets'),
    path('author/' , views.author , name='author'),
    path('single/' , views.single , name='single'),
   
]