from django.urls import path
from .views import UserSignUp, EditProfile, PasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

#from .view import ContactView
urlpatterns = [

    path('register/',UserSignUp.as_view(), name='signup'),
    path('edit_profile/',EditProfile.as_view(), name='edit_profile'),
    path('password/',PasswordChangeView.as_view()),
    path('password_succes/',views.password_success,name='password_success'),
]