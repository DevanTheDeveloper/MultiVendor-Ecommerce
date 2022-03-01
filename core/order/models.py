from django.db import models
from product.models import Product
from vendor.models import Vendor

from django.contrib.auth.models import User

from phone_field import PhoneField


class Order(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone = PhoneField()
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)
	
	state = models.CharField(max_length=30)
	zipcode = models.CharField(max_length=6 )
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	confirmed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
	vendors = models.ManyToManyField(Vendor,related_name="orders")
	user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE, blank=True, null=True)

	pay_option = models.CharField(max_length=10)
	invoice_id = models.CharField(max_length=30)
	
	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return str(self.pk)

	@property
	def get_cart_total(self):
		orderitems = self.items.all()
		total = sum([item.get_total_price() for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.items.all()
		total = sum([item.quantity for item in orderitems])
		return total
	


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
	product = models.ForeignKey(Product,related_name="items", on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor, related_name="items", on_delete=models.CASCADE)
	vendor_paid = models.BooleanField(default=False)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return str(self.order.pk)

	def get_total_price(self):
		return int(self.price * self.quantity)