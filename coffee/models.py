from django.db import models

# Create your models here.
class coffee(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock_qt=models.IntegerField()
    image=models.CharField(max_length=2083)
