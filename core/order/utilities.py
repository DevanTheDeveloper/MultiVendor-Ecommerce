from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from cart.cart import Cart

from .models import Order, OrderItem
from product.models import Product, Stock


def notify_vendor(order):

	for vendor in order.vendors.all():
		from_email = settings.DEFAULT_FROM_EMAIL
		to_email = vendor.email
		subject = "New Order"
		text_content = "You have a new order!"
		context = {
					'order':order,
					'vendor':vendor
		}
		html_content = render_to_string('order/email_notify_vendor.html',context)

		msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
		msg.attach_alternative(html_content,'text/html')
		msg.send()

def notify_customer(order):
	from_email = settings.DEFAULT_FROM_EMAIL

	to_email = order.email
	subject = 'Order Confirmation'
	text_content = 'Thank you for the order!'
	context={
				'order':order

	}
	html_content = render_to_string('order/email_notify_customer.html',context)

	msg = EmailMultiAlternatives(subject,text_content, from_email, [to_email])
	msg.attach_alternative(html_content, 'text/html')
	msg.send()
	

def checkout(request, first_name,last_name, email, address1,address2,zipcode,city,state,country,phone,amount,pay_option ):
	order = Order.objects.create(  first_name=first_name,
									last_name=last_name,
									email=email,
									address1=address1,
									address2=address2,
									city=city,
									state=state,
									country=country,
									zipcode=zipcode,
									phone=phone,
									paid_amount=amount,
									pay_option=pay_option
									)

	if request.user.is_authenticated:
		order.user = request.user
		order.save()

	for item in Cart(request):
		OrderItem.objects.create(order=order, 
								product=item['product'],
								vendor=item['product'].vendor,
								price=item['product'].price,
								quantity=item['quantity']

								)
		order.vendors.add(item['product'].vendor)

		product = Product.objects.get(pk=item['id'])
		productStock = Stock.objects.get(product=product)
		productStock.units -= item['quantity']
		productStock.units_sold += item['quantity']
		productStock.save()


	return order