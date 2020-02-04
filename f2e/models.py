from django.db import models
from .static import ORDER_STATUS

class Order(models.Model):
    name = models.TextField()
    logo = models.URLField()
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    date = models.DateField()
