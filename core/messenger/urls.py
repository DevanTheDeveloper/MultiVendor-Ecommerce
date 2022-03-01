from django.urls import path
from . import views

urlpatterns = [
				path('send/<int:pk>/',views.createThread, name='createThread'),
				path('<int:pk>/', views.threadView, name='thread'),
				path('inbox/', views.inbox, name='inbox'),
				path('vendor/inbox',views.vendorInbox,name="vendorInbox")

]