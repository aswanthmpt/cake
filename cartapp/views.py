from django.shortcuts import render
from demoapp.models import Product

# Create your views here.
def cart(req,id):
    return render(req,'cart.html')
