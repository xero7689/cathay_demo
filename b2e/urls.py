from django.urls import path
from . import views

urlpatterns = [
    path('<str:short_path>', views.b2e, name='b2e_short_path'),
    path('', views.b2e, name='b2e'),
    path('shortener/', views.shortener, name='b2e_shortener'),
]
