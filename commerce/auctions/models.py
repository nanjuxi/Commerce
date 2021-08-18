from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class auction_listing(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    price = models.IntegerField()
    description = models.TextField(blank=True)

    def __self__(self):
        return f"{self.name} {self.image} {self.price} {self.description}"


class  bid(models.Model):
    nowPrice = models.IntegerField()
    bidPrice = models.IntegerField()

    def __self__(self):
        return f"{self.nowPrice} {self.bidPrice}"

class comment(models.Model):
    comment = models.TextField()

    def __self__(self):
        return f"{self.comment}"
