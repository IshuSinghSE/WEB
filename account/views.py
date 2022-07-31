from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserEditForm, PasswordEditForm, ProfilePageForm
from theblog.models import profile, post 

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def login_user(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
				login(request, user)
				messages.success(request, ("Welcome @" + username + " have Logged in Successfuly! "))
				return redirect('index')
		else:
			messages.error(request, ("Something went wrong, Try Again! "))
			return redirect('login')

	else:	
		return render(request, 'registration/login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, "You have Logged Out Successfuly! ")
	return redirect('index')


# Create your views here.
class ShowProfile(DetailView):
	model = profile 
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
	    users = profile.objects.all()
	    context = super(ShowProfile, self).get_context_data(*args, **kwargs)
	    page_user = get_object_or_404(profile, id=self.kwargs['pk'])
	    context["page_user"] = page_user
	    return context



class EditProfilePage(generic.UpdateView):
	model = profile
	template_name = 'registration/edit_profile_page.html'
	fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'pinterest_url']
	success_url = reverse_lazy('index')
	#messages.success(request, ("You have Profile Updated Successfuly! "))


class CreateProfilePage(generic.CreateView):
	model = profile
	template_name = 'registration/create_profile_page.html'
	form_class = ProfilePageForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


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
	messages.success(request, ("Password changed Successfuly! "))
	return render(request, 'registration/password_success.html',{})
