from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vendor(models.Model):
	owner = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
	title = models.CharField(max_length=255,verbose_name='Store/Vendor Title')
	email = models.CharField(max_length=255, verbose_name='E-mail', blank=True,null=True)
	description = models.TextField(max_length=500,blank=True, null=True,verbose_name="Description")

	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	views = models.IntegerField(default=0)
	city = models.CharField(max_length=255, blank=True, null=True, verbose_name="City")
	state = models.CharField(max_length=255,blank=True, null=True, verbose_name="State/Province")
	address1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address Line 1")
	address2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address Line 2")
	zipcode = models.CharField(max_length=8, blank=True, null=True, verbose_name='Zip/Postal Code')
	
	class Meta:
		ordering = ['title']

	def __str__(self):
		return str(self.title)


	def get_unpaid_balance(self):
		items = self.items.filter(vendor_paid=False,order__vendors__in=[self.id])
		return sum((item.product.price * item.quantity) for item in items)


	def get_paid_balance(self):
		items = self.items.filter(vendor_paid=True,order__vendors__in=[self.id])
		return sum((item.product.price * item.quantity) for item in items)

class VendorReview(models.Model):

	class Rating(models.TextChoices):
	    POOR = '1', "Unsatisfied"
	    BELOW = '2', "Below Average"
	    AVERAGE = '3', "Average"
	    ABOVE = '4','Above Average'
	    EXCELLENT = '5','Excellent'
	    # (...)

	rating = models.CharField(max_length=2,choices=Rating.choices,default=Rating.AVERAGE)
	vendor = models.ForeignKey(Vendor, related_name='vendorReviews', on_delete=models.CASCADE)
	writer = models.ForeignKey(User, related_name='vendorReviews', on_delete=models.CASCADE)
	comment = models.TextField(max_length=500)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def verified(self):
		writer = self.writer
		
		if self.vendor.orders.filter(user__username=writer):
			return True

		else:
			return False
