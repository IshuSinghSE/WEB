from django.urls import path
from .views import UserSignUp, EditProfile, PasswordChangeView, ShowProfile, EditProfilePage, CreateProfilePage, login_user, logout_user
from django.contrib.auth import views as auth_views
from . import views

#from .view import ContactView
urlpatterns = [

    path('register/',UserSignUp.as_view(), name='signup'),
    path('edit_profile/',EditProfile.as_view(), name='edit_profile'),
    path('password/',PasswordChangeView.as_view()),
    path('password_success/',views.password_success,name='password_success'),
    path('<int:pk>/profile/',ShowProfile.as_view(), name='show_profile'),
    path('<int:pk>/edit_profile_page/',EditProfilePage.as_view(), name='edit_profile_page'),
    path('create_profile_page/',CreateProfilePage.as_view(), name='create_profile_page'),

    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),

]