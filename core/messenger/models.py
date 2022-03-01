from django.db import models
from django.contrib.auth.models import User

from vendor.models import Vendor 
# Create your models here.

class Thread(models.Model):
	#Host, topic, participants  == foreign keys
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,blank=True, null=True)
	subject = models.CharField(max_length=400, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['-updated','-created']

	def __str__(self):
		return str(self.id)


class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	thread = models.ForeignKey(Thread, related_name='messages', on_delete=models.CASCADE)
	content = models.TextField(max_length=500,verbose_name="Send a Message:")
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.content[:50]

	class Meta:
		ordering = ['-updated','-created']