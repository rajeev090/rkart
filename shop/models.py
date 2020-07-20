from django.db import models
from .category import cat, sub_cat
from django.utils import timezone

# Create your models here.


class Product(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50, choices=cat(), default="")
    subcategory = models.CharField(
        max_length=50, choices=sub_cat(), default="")
    brand = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=1500)
    price = models.FloatField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):

    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="",
                            editable=False)
    email = models.CharField(max_length=50, default="", editable=False)
    phone = models.CharField(max_length=15, default="", editable=False)
    msgtype = models.CharField(max_length=15, default="", editable=False)
    message = models.TextField(editable=False)
    date = models.DateTimeField(
        editable=False, default=timezone.now)

    def __str__(self):
        return self.name
