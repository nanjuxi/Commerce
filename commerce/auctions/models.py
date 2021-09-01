from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    # name = models.CharField(max_length=50)
    # password = models.CharField(max_length=20)
    #
    # def __self__(self):
    #     return f"{self.name} {self.password}"

class Product(models.Model):
    objectName = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    startBid = models.FloatField()
    image = models.ImageField(upload_to='images/')
    Select = models.IntegerField()




class auction_listing(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    price = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.image} {self.price} {self.description}"


class  bid(models.Model):
    nowPrice = models.IntegerField()
    bidPrice = models.IntegerField()

    def __str__(self):
        return f"{self.nowPrice} {self.bidPrice}"

class comment(models.Model):
    comment = models.TextField()

    def __str__(self):
        return f"{self.comment}"


class object(models.Model):
    name = models.CharField(max_length=100)
    descroption = models.CharField(max_length=2000)
    price = models.FloatField()
    image = models.BinaryField()

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.image}"