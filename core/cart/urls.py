from django.urls import path
from . import views

urlpatterns = [

				path('', views.cartDetail, name="cart"),
				path('success/',views.success,name="success"),
				
]