from django.urls import path

from .import views

urlpatterns = [ 


	path('category/<slug:category_slug>/', views.productCategory, name='productCategory'),
	path('vendors/category/<slug:vendorCategory_slug>/',views.vendorCategory, name='vendorCategory'),
	path('product/<slug:category_slug>/<slug:product_slug>/',views.productDetail, name='productDetail'),
	path('search/', views.search, name='search'),
	path('product-review/<slug:category_slug>/<slug:product_slug>/', views.productReview, name="productReview"),


	]