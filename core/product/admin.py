from django.contrib import admin
from .models import Category,Product, ProductImage,SubCategory,ProductReview, Stock
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(SubCategory)
admin.site.register(ProductReview)
admin.site.register(Stock)