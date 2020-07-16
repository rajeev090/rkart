from django.db import models
from .catagory import cat, sub_cat

# Create your models here.


class Product(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    catagory = models.CharField(
        max_length=50, choices=cat())
    subcatagory = models.CharField(
        max_length=50, choices=sub_cat())
    brand = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=1500)
    price = models.FloatField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name
