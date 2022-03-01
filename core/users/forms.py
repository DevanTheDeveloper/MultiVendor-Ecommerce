from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,UserShipping



class UserRegisterForm(UserCreationForm):
	email= forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()


	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2','first_name', 'last_name']

		field_order = ['username','first_name', 'last_name', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:

		model = User
		fields = ['username', 'email']
		#fields = ['username', 'email', 'phone', 'address', 'city', 'province', 'postalcode', 'drivers_front', 'holding_card','image' ]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model= Profile
		fields= ['image']

class UserShippingForm(forms.ModelForm):
	class Meta:
		model= UserShipping
		fields= ['first_name','last_name','address1','address2','city','state',
					'country','zipcode','phone']


		


