from django.urls import path
from . import views

urlpatterns = [
    path('', views.f2e, name='f2e'),
    path('orders/', views.orders, name='orders')
]
