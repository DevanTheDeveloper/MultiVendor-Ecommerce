from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.paginator import Paginator

from django.utils.text import slugify

from .forms import VendorUpdateForm,VendorReviewForm, SubCategoryForm
from cart.forms import ResultForm
from product.forms import ProductForm, ProductImageForm

from .models import Vendor
from product.models import ProductImage


# Create your views here.
def addSubCategory(request):
	if request.method == "POST":
		form = SubCategoryForm(request.POST)
		if form.is_valid():
			newCategory = form.save(commit=False)
			newCategory.slug = slugify(form.cleaned_data['title'])
			newCategory.save()
			messages.success(request, 'A new SubCategory for %s has been added!' % newCategory.title )
			return redirect('vendorAdmin')

	form = SubCategoryForm()
	context = {'form':form}
	return render(request, 'vendor/addSubCategory.html', context)


def vendorReview(request,pk):

	vendor = get_object_or_404(Vendor, pk=pk)

	if request.method == "POST" and request.user.is_authenticated:
		form = VendorReviewForm(request.POST)
		if form.is_valid():
			newReview = form.save(commit=False)
			newReview.vendor = vendor
			newReview.writer = request.user
			newReview.save()
			messages.success(request,'Thank you for the review!')
			return redirect('vendor', vendor.id)

	context = {
				'form':VendorReviewForm(),
				'vendor':vendor
	}

	return render(request,'vendor/vendorReview.html',context)	

def vendorInfo(request,pk):

	vendor = get_object_or_404(Vendor, pk=pk)



	context = {
				'vendor':vendor
	}
	return render(request,'vendor/vendorInfo.html',context)



def vendor(request,pk, price=None,vendorCategory=None):

	vendor = get_object_or_404(Vendor, pk=pk)

	perPage = request.GET.get('perPage',5)
	resForm = ResultForm(initial={'perPage':perPage})
	products = vendor.products.all()

	paginator = Paginator(products,perPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)



	vendor.views += 1
	vendor.save()

	context = {
				'vendor':vendor,
				'page_obj':page_obj,
				'resForm':resForm,			
	}
	return render(request,'vendor/vendor.html',context)

def vendorList(request):
	vendors = Vendor.objects.all()
	context = {
				'vendors':vendors
				}

	return render(request, 'vendor/vendorList.html', context)


def vendorRegister(request):
	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()

			login(request,user)

			vendor = Vendor.objects.create(title=user.username, owner=user)

			return redirect('index')

	context = {'form':UserCreationForm() }
	return render(request, 'vendor/register.html', context)


@login_required
def vendorAdmin(request):
	
	perPage = request.GET.get('perPage',5)
	resForm = ResultForm(initial={'perPage':perPage})
	vendor = request.user.vendor
	products = vendor.products.all()
	orders = vendor.orders.all()
	paginator = Paginator(orders,perPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)


	for order in orders:
		order.vendor_amount = 0
		order.vendor_paid_amount = 0 
		order.fully_paid = True

		for item in order.items.all():
			if item.vendor == request.user.vendor:
				if item.vendor_paid: 
					order.vendor_paid_amount += item.get_total_price()
				else:
					order.vendor_amount += item.get_total_price()
					order.fully_paid = False

	context = { 'vendor':vendor,
				'products':products,
				'page_obj':page_obj,
				'resForm':resForm,
				
				}
	return render(request,'vendor/admin.html',context)


@login_required
def addProduct(request):

	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			newProduct = form.save(commit=False)
			newProduct.vendor = request.user.vendor
			newProduct.slug = slugify(newProduct.title)
			newProduct.save()

			return redirect('vendorAdmin')
	form = ProductForm()

	context= { 'form':form}
	return render(request, 'vendor/addProduct.html',context)

@login_required
def updateProduct(request,pk):
	vendor = request.user.vendor
	product = vendor.products.get(pk=pk)
	productImages = product.images.all()


	
	form = ProductForm(instance=product)
	ImageFormSet = modelformset_factory(ProductImage,fields=('title','image'),extra=2)
	imageForm = ImageFormSet(queryset=ProductImage.objects.filter(product=product))

	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES,instance=product)
		imageForm = ImageFormSet(request.POST, request.FILES)

		if imageForm.is_valid():
			for image in imageForm:
				newImage = image.save(commit=False)
				newImage.product = product
				newImage.save()
				messages.success(request,'Product Images Updated!')
				return redirect('vendorAdmin')
		elif form.is_valid():
			form.save()		
			messages.success(request,'Product Updated!')
			return redirect('vendorAdmin')

	context = {'form':form,
				'product':product,
				'productImages':productImages,
				'imageForm':imageForm }
	return render(request, 'vendor/updateProduct.html',context)


@login_required
def vendorEdit(request):
	vendor = request.user.vendor
	form = VendorUpdateForm(instance=vendor)
	if request.method == "POST":
		form = VendorUpdateForm(request.POST,instance=vendor)
		if form.is_valid():
			update = form.save()
			messages.success(request, 'Vendor Profile Updated!')


			return redirect('vendorAdmin')

	context = {
				'vendor':vendor,
				'form':form

	}

	return render(request, 'vendor/vendorEdit.html',context)