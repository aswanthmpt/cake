from django.shortcuts import render,redirect
from demoapp.models import Product
from .models import Cart
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    
    try:
        cartitem=Cart.objects.get(user=user,products=product)
        if cartitem.quantity<cartitem.products.stock:
            cartitem.quantity+=1
            cartitem.price=cartitem.products.price*cartitem.quantity
            cartitem.save()
            
    except ObjectDoesNotExist:
            cartitem=Cart.objects.create(user=user,products=product,quantity=1,price=product.price)
            cartitem.save()
    return redirect('cart:displaycart')

def displaycart(req):
    user=req.session['user']
    
    
    
    cart=Cart.objects.all().filter(user=user)
    totalprice=sum(item.price for item in cart)
    
    
    return render(req,'cart.html',{"cart":cart,"totalprice":totalprice})
def delete(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(user=user,products=product)
    cart.delete()
    return redirect('cart:displaycart')
