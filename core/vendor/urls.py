from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [ path('become-vendor/',views.vendorRegister, name='vendorRegister'),
				path('admin/',views.vendorAdmin,name='vendorAdmin'),
				path('logout/', auth_views.LogoutView.as_view(), name='vendor_logout'),
				path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='vendor_login'),
				path('add/product/',views.addProduct, name='addProduct'),
				path('update-product/<int:pk>',views.updateProduct, name='updateProduct'),
				path('edit/',views.vendorEdit, name='vendorEdit'),
				path('',views.vendorList,name='vendorList'),
				path(r'<int:pk>/', views.vendor, name='vendor'),
				path('reviews/<int:pk>/',views.vendorReview,name='vendorReview'),
				path('vendor-info/<int:pk>/', views.vendorInfo, name='vendorInfo'),
				path('add/subcategory/', views.addSubCategory, name='addSubCategory'),







]