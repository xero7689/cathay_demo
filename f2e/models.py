from django.db import models
from .static import ORDER_STATUS, ORDER_STATUS_DICT

class Order(models.Model):
    name = models.TextField()
    logo = models.URLField()
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
    date = models.DateField()

    @property
    def deal_type(self):
        return ORDER_STATUS_DICT[self.status]

