from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from cart.forms import ResultForm
from .models import Order

# Create your views here.
@login_required
def cxOrders(request):
	orders = Order.objects.filter(user=request.user)
	perPage = request.GET.get('perPage',5)
	resForm = ResultForm(initial={'perPage':perPage})

	paginator = Paginator(orders,perPage)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)



	
	context = {
				'page_obj':page_obj,
				'resForm':resForm,
				}
	return render(request, 'order/cx_orders.html', context)