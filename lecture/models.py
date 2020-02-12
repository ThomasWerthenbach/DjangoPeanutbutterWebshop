from django.db import models

class PeanutButter(models.Model):
    brand = models.CharField(max_length=50)
    picture_address = models.CharField(max_length=500)
    price = models.FloatField(default=0.0)

