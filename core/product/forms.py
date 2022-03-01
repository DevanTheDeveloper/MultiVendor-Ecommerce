from django import forms
from django.forms import ModelForm
from . models import Product, ProductImage, ProductReview


class ProductReviewForm(ModelForm):
	class Meta:
		model = ProductReview
		fields = ['rating','comment']

class ProductImageForm(ModelForm):
	class Meta:
		model = ProductImage
		fields = ['image','title']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['category','subcategory','image','title','description','price']



class AddToCartForm(forms.Form):
	quantity = forms.IntegerField()