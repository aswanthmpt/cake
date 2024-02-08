from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
# Create your views here.
def home(req):
    product=Product.objects.all()
    return render(req,'index.html',{"product":product})
