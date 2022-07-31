from django import forms
from .models import post, category, Comment


choices = category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
   choice_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = post 
		fields = ('title','author','category','body','image', 'snippet', 'status')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
		'author': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id':'author', 'type':'hidden'}),
		'category': forms.Select(choices=choice_list,attrs={'class': 'form-control form-control-lg'}),
		'body': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
		'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
		'snippet': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
		'status': forms.Select(attrs={'class': 'form-control form-control-lg'}),

		}

class EditForm(forms.ModelForm):
	class Meta:
		model = post 
		fields = ('title','category','body','image', 'snippet', 'status')
		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
		'author': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
		'category': forms.Select(choices=choice_list, attrs={'class': 'form-control form-control-lg'}),
		'body': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
		'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
		'snippet': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
		'status': forms.Select(attrs={'class': 'form-control form-control-lg'}),


		}
