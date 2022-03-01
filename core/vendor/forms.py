from django.forms import ModelForm

from .models import Vendor, VendorReview

from product.models import SubCategory

class VendorReviewForm(ModelForm):
	class Meta:
		model = VendorReview
		fields = ['rating','comment']

class VendorUpdateForm(ModelForm):
	class Meta:
		model = Vendor
		fields = ['title','email','city','state','description']

class SubCategoryForm(ModelForm):
	class Meta:
		model = SubCategory
		fields = ['title']