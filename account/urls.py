from django.urls import path
from .views import UserSignUp


#from .view import ContactView
urlpatterns = [

    path('register/',UserSignUp.as_view(), name='signup'),

]