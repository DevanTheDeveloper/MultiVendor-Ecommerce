from django.db import models
from django.core.files import File
from PIL import Image
from io import BytesIO


from django.contrib.auth.models import User
from vendor.models import Vendor


# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	ordering = models.IntegerField(default=0)

	class Meta:
		ordering = ['ordering']

	def __str__(self):
		return self.title 

class SubCategory(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank=True, null=True)
	ordering = models.IntegerField(default=0)
	vendor = models.ForeignKey(Vendor,related_name='subcategory', verbose_name='Vendor', on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		ordering = ['ordering']

	def __str__(self):
		return self.title 

class Stock(models.Model):
	product = models.OneToOneField('product',related_name='stock', on_delete=models.CASCADE, blank=True, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	units = models.IntegerField(default=0)
	units_sold = models.IntegerField(default=0)


	def __str__(self):
		return self.product.title

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,blank=True, null=True)
	subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE,blank=True, null=True)
	vendor = models.ForeignKey(Vendor, related_name = 'products', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	created = models.DateTimeField(auto_now=True, auto_now_add=False)
	date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
	image = models.ImageField(upload_to='uploads/', blank=True,null=True)
	thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)


	class Meta:
		ordering = ['-date_added']

	def __str__(self):
		return self.title

	def get_thumbnail(self):
		if self.image:
			self.thumbnail = self.make_thumbnail(self.image)
			self.save()

			return self.thumbnail.url

		else:
			return 'https://via.placeholder.com/240x180.jpg'

	def make_thumbnail(self,image,size=(300,200)):
		img = Image.open(image)
		img.convert('RGB')
		img.thumbnail(size)

		thumb_io = BytesIO()
		img.save(thumb_io,'JPEG',quality=85)

		thumbnail = File(thumb_io, name=image.name)

		return thumbnail  


class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='uploads/', blank=True,null=True)
	title = models.CharField(max_length=255)
	thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

	def get_thumbnail(self):
		if self.image:
			self.thumbnail = self.make_thumbnail(self.image)
			self.save()

			return self.thumbnail.url

		else:
			return 'https://via.placeholder.com/240x180.jpg'

	def make_thumbnail(self,image,size=(300,200)):
		img = Image.open(image)
		img.convert('RGB')
		img.thumbnail(size)

		thumb_io = BytesIO()
		img.save(thumb_io,'JPEG',quality=85)

		thumbnail = File(thumb_io, name=image.name)

		return thumbnail  

class ProductReview(models.Model):

	class Rating(models.TextChoices):
	    POOR = '1', "Unsatisfied"
	    BELOW = '2', "Below Average"
	    AVERAGE = '3', "Average"
	    ABOVE = '4','Above Average'
	    EXCELLENT = '5','Excellent'
	    # (...)

	rating = models.CharField(max_length=2,choices=Rating.choices,default=Rating.AVERAGE)
	product = models.ForeignKey(Product, related_name='productReviews', on_delete=models.CASCADE)
	writer = models.ForeignKey(User, related_name='productReviews', on_delete=models.CASCADE)
	comment = models.TextField(max_length=500)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	verified = models.BooleanField(default=False)

	def __str__(self):
		return str(self.product.title)

	def save(self, *args, **kwargs):
		

	
		if self.product.items.filter(order__user__username=self.writer):
			self.verified = True
		else:
			self.verified = False

		super().save(*args, **kwargs)


class ProductQuestions(models.Model):

	product = models.ForeignKey(Product, related_name='productQuestions', on_delete=models.CASCADE)
	writer = models.ForeignKey(User, related_name='productQuestions', on_delete=models.CASCADE)
	comment = models.TextField(max_length=500)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)	

class ProductAnswers(models.Model):
	product = models.ForeignKey(Product, related_name='productAnswers', on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor,related_name='productAnswers', on_delete=models.CASCADE)
	comment = models.TextField(max_length=500)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
