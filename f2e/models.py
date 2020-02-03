from django.db import models

class Order(models.Model):
    name = models.TextField()
    logo = models.URLField()
    status = models.IntegerField()
    date = models.DateField()
