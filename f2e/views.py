from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.core import serializers
from django.template.loader import render_to_string

from .models import Order
from .serializers import OrdersPythonSerializer

def f2e(request):
    return render(request, 'f2e.html')

def orders(request):
    response = {
        'orders': []
    }

    if request.method == 'GET':
        serializer = OrdersPythonSerializer()
        orders = serializer.serialize(Order.objects.all())
        response['orders'] = orders

    return JsonResponse(response)
