from django.shortcuts import render
from django.core.paginator import Paginator

from product.models import Product
from cart.forms import ResultForm


# Create your views here.
def index(request):
	
	products = Product.objects.all()
	perPage = request.GET.get('perPage',5)
	resForm = ResultForm(initial={'perPage':perPage})

	paginator = Paginator(products,perPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)



	context = {'products':products,
				'page_obj':page_obj,
				'resForm':resForm,

	}

	return render(request, 'site/index.html',context)


def contact(request):
	return render(request, 'site/contact.html')