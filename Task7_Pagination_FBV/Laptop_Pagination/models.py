from django.db import models

# Create your models here.
class Laptops(models.Model):
    Model_Name=models.CharField(max_length=50)
    Provider=models.CharField(max_length=50)
    RAM=models.IntegerField()
    ROM=models.IntegerField()
    Processor=models.CharField(max_length=50)
    Weight=models.FloatField()
    Price=models.FloatField()