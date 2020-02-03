from django.test import TestCase
from .models import Order

class OrdersTestCase(TestCase):
    def test_saving_and_retrieving(self):
        order = Order()
        order.name = 'Apple Airpods 2'
        order.logo = 'https://static.oopocket.com/store/iconTreemall@3x.png'
        order.status = 4
        order.date = '2019-03-02'
        order.save()

        orders = Order.objects.all()
        self.assertEqual(orders.count(), 1)
        self.assertEqual(orders[0].name, 'Apple Airpods 2')

