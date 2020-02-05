from django.urls import path
from . import views

urlpatterns = [
    path('', views.b2e, name='b2e'),
    path('shortener/', views.shortener, name='b2e_shortener'),
]
