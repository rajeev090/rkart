from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your tests here.
# m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# m.sort(reverse=True)
# y = m[0:5]
# print(y)

blogpost = Blogpost.objects.all()
n = [blogpost]
print(n)
