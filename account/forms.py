from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

	class Meta:
		model = User 
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'	
		self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
		self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'

'''
class UserChangeForm(UserChangeForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

	class Meta:
		model = User 
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'	
		self.fields['password1'].widget.attrs['class'] = 'form-control form-control-lg'
		self.fields['password2'].widget.attrs['class'] = 'form-control form-control-lg'

'''