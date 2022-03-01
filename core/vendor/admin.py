from django.contrib import admin
from .models import Vendor, VendorReview


# Register your models here.
admin.site.register(VendorReview)
admin.site.register(Vendor)