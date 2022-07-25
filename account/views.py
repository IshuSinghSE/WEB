from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UserChangeForm
# Create your views here.

class UserSignUp(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

class EditProfile(generic.UpdateView):
	form_class = UserChangeForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('index')

	def get_object(self):
		return self.request.user