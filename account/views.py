from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserEditForm, PasswordEditForm

# Create your views here.

class UserSignUp(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')

	
class EditProfile(generic.UpdateView):
	form_class = UserEditForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('index')

	def get_object(self):
		return self.request.user

class PasswordChangeView(PasswordChangeView):
	form_class = PasswordEditForm
	template_name='registration/change_password.html'
	success_url = reverse_lazy('password_success')

def password_success(request):
	return render(request, 'registration/password_success.html',{})
