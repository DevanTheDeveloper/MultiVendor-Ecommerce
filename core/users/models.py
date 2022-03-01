from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', verbose_name='Profile Image', upload_to='profile_pics')
	created = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail (output_size)
			img.save(self.image.path)


class UserShipping(models.Model):
	user = models.OneToOneField(User, related_name='shipping', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255,verbose_name='First Name', blank=True,null=True)
	last_name = models.CharField(max_length=255,verbose_name='Last Name', blank=True,null=True)
	address1 = models.CharField(max_length=255, verbose_name='Address Line 1', blank=True,null=True)
	address2 = models.CharField(max_length=255, verbose_name='Address Line 2', blank=True,null=True)
	city = models.CharField(max_length=255, verbose_name='City', blank=True,null=True)
	state = models.CharField(max_length=255, verbose_name='State/Province', blank=True,null=True)								
	country = models.CharField(max_length=255, verbose_name='Country', blank=True,null=True)
	zipcode = models.CharField(max_length=255, verbose_name='Zip/Postal Code', blank=True,null=True)
	phone = models.CharField(max_length=255, verbose_name='Phone Number', blank=True,null=True)
	

	def __str__(self):
		return self.user.username