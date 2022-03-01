from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings



import random
from cart.forms import ResultForm
from cart.cart import Cart
from .models import Category, Product, SubCategory

from .forms import AddToCartForm, ProductReviewForm



def search(request):
	if request.method == "GET":
		
		query = request.GET.get('query','')
		products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

		context = { 'products':products,
					'query':query}
		

		return render(request, 'product/search.html', context)

@login_required
def productReview(request, category_slug, product_slug):

	product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

	if request.method == "POST":
		form = ProductReviewForm(request.POST)
		if form.is_valid():
			newReview = form.save(commit=False)
			newReview.writer = request.user
			newReview.product = product
			newReview.save()
			messages.success(request,'Thanks for leaving a Review!')			
		else:
			messages.error(request,'Uh oh, something went wrong!')
		return redirect('productDetail',category_slug, product_slug)

	context = {'form':ProductReviewForm(),
				'product':product,
				'reviews':product.productReviews.all().order_by('-created')}

	return render(request, 'product/productReview.html', context)

def productDetail(request, category_slug, product_slug):

	cart = Cart(request)

	product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

	imagesString = '{"thumbnail":"%s", "image":"%s","id":"mainImage"},' % (product.get_thumbnail(),product.image.url)
	
	for image in product.images.all():
		imagesString += '{"thumbnail":"%s", "image":"%s","id":"%s"},' % (image.get_thumbnail(),image.image.url,image.id)  
	
	

	if request.method == "POST":
		form = AddToCartForm(request.POST)

		if form.is_valid():
			quantity = form.cleaned_data['quantity']
			cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
			messages.success(request,'Product was added to cart!')

			return redirect(request.META.get('HTTP_REFERER'))
	else:
		form = AddToCartForm()

	similar_products = list(product.category.products.exclude(id=product.id))
	print(similar_products)

	if len(similar_products) >=5:
		similar_products = random.sample(similar_products,5)

	context = { 'product':product, 
				'similar':similar_products,
				'form':form,
				'imagesString':"["+ imagesString.rstrip(',') +"]" ,
				'reviews':product.productReviews.all().order_by('-created')
				}
	
	return render(request,'product/detailProduct.html',context)

def productCategory(request, category_slug):
	
	category = get_object_or_404(Category,slug=category_slug)
	products = category.products.all()


	perPage = request.GET.get('perPage',5)
	resForm = ResultForm(initial={'perPage':perPage})
	

	paginator = Paginator(products,perPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {

				'category':category,
				'page_obj':page_obj,
				'resForm':resForm,		
	}
	return render(request, 'product/category.html', context )

def vendorCategory(request, vendorCategory_slug):
	
	vendorCategory = get_object_or_404(SubCategory,slug=vendorCategory_slug)
	products = vendorCategory.products.all()

	perPage = request.GET.get('perPage',5)
	resForm = ResultForm(initial={'perPage':perPage})
	
	paginator = Paginator(products,perPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {

			'category':vendorCategory,
			'page_obj':page_obj,
			'resForm':resForm,	
	}
	return render(request, 'product/category.html', context )