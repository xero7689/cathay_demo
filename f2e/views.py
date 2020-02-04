from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template.loader import render_to_string

from .models import Order
from .static import ORDER_STATUS_DICT

def f2e(request):
    return render(request, 'f2e.html')

def orders(request):
    response = {
        'orders': []
    }

    if request.method == 'GET':
        orders = Order.objects.all()
        orders = serializers.serialize('python', orders)
        for order in orders:
            order['fields']['type'] = ORDER_STATUS_DICT[order['fields']['status']]
            print(order)
            response['orders'].append(order['fields'])

    return JsonResponse(response)
