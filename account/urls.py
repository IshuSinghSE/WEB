from django.urls import path
from .views import UserSignUp, EditProfile


#from .view import ContactView
urlpatterns = [

    path('register/',UserSignUp.as_view(), name='signup'),
    path('edit_profile/',EditProfile.as_view(), name='edit_profile'),

]