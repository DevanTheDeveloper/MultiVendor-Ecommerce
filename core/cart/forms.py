from django import forms
from phone_field import PhoneField


class checkoutForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=50)
	phone = forms.CharField(max_length=50,
		widget=forms.TextInput(attrs={'placeholder': 'eg. (123)-456-7890'}))
	address1 = forms.CharField(
	    label='Address Line 1',
	    widget=forms.TextInput(attrs={'placeholder': 'Street Address'})
	)
	address2 = forms.CharField( label="Address Line 2",
	    widget=forms.TextInput(attrs={'placeholder': 'Apartment, Suite, or Unit'})
	)
	state = forms.CharField(label="Province/State",max_length=30)
	zipcode = forms.CharField(max_length=6, label="Zip/Postal Code")
	city = forms.CharField(max_length=30)
	country = forms.CharField(max_length=30)
	confirmed = forms.BooleanField(required=True,label="All information provided is accurate and true")
	

class ResultForm(forms.Form):

	perPage = forms.MultipleChoiceField(choices=((5, ("5")),
	                                        (10, ("10")),
	                                        (25, ("25")),
	                                        (50, ("50")),
	                                        (100, ("100"))),
	                                required=False, label='Results Per Page:',
	                                widget = forms.Select(attrs = {'onchange' : "Result();"}))



