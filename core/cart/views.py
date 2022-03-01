import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,redirect 
from django.http import JsonResponse

from . forms import checkoutForm
from .cart import Cart  
from order.utilities import checkout, notify_vendor, notify_customer



# Create your views here.


def success(request):
	return render(request,'cart/success.html')


def cartDetail(request):
	
	cart=Cart(request)
	from product.models import Product
	#for item in cart:
		#print( Product.objects.get(pk=item['id']))

	if request.user.is_authenticated:
		form = checkoutForm()

	else:	
		form = checkoutForm()
	if request.method == "POST":
		print(request.POST)
		form = checkoutForm(request.POST)
		if form.is_valid():

			pay_option = request.POST.get('pay_option')
			print(pay_option)
			if pay_option == "stripe":

				stripe.api_key = settings.STRIPE_SECRET_KEY

				try:

					stripe_token = request.POST.get('stripe_token')
					charge = stripe.Charge.create(
									amount = int(cart.get_total_cost() * 100 ), #stripe only takes cents
									currency = 'USD',
									description = 'Charge from InteriorShop',
									source=stripe_token
												)

					first_name = form.cleaned_data['first_name']
					last_name = form.cleaned_data['last_name']
					email = form.cleaned_data['email']
					phone = form.cleaned_data['phone']
					address1 = form.cleaned_data['address1']
					address2 = form.cleaned_data['address2']
					zipcode = form.cleaned_data['zipcode']
					city = form.cleaned_data['city']
					state = form.cleaned_data['state']
					country = form.cleaned_data['country']

					

					order = checkout(request,
									first_name,
									last_name,
									email,
									address1,
									address2,
									zipcode,
									city,
									state,
									country,
									phone,
									cart.get_total_cost(),
									pay_option )  

					
					cart.clear()

					notify_customer(order)
					notify_vendor(order)
					messages.success(request,'Processed!')
					return redirect('success')

				except Exception as e:
					print(e)
					messages.error(request,"Something went wrong with the processing of your payment")
			
			elif pay_option == "paypal":

				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				email = form.cleaned_data['email']
				phone = form.cleaned_data['phone']
				address1 = form.cleaned_data['address1']
				address2 = form.cleaned_data['address2']
				zipcode = form.cleaned_data['zipcode']
				city = form.cleaned_data['city']
				state = form.cleaned_data['state']
				country = form.cleaned_data['country']

				

				order = checkout(request,
								first_name,
								last_name,
								email,
								address1,
								address2,
								zipcode,
								city,
								state,
								country,
								phone,
								cart.get_total_cost(),
								pay_option, )  

				
				cart.clear()

				notify_customer(order)
				notify_vendor(order)
				messages.success(request,'Thank you for your payment!')
				return JsonResponse('Payment Processed', safe=False)

		
		else:
			print(form.errors)
			form = checkoutForm()

	remove_from_cart = request.GET.get('remove_from_cart','')
	change_quantity = request.GET.get('change_quantity','')

	
	quantity = request.GET.get('quantity',0)

	if remove_from_cart:
		cart.remove(remove_from_cart)
		return redirect('cart')

	if change_quantity:
		print("changequantity",change_quantity,"quantity=", quantity)
		cart.add(change_quantity,quantity,True)
		print('3tester')
		return redirect('cart')

	context = {'checkoutForm':form,
				'stripe_pub_key':settings.STRIPE_PUB_KEY,
				'paypal_key':settings.PAYPAL_KEY}

	return render(request, 'cart/cartDetail.html', context)