from django.shortcuts import render,get_object_or_404,redirect

from . models import Product,Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(req,c_slug=None):
    product=None
    c_page=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product=Product.objects.all().filter(category=c_page,available=True)
    else:
        product=Product.objects.all().filter(available=True)
        
    paginator=Paginator(product,2)
    try:
        page=int(req.GET.get('page'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
        
    
    return render(req,'index.html',{"product":products,"cat":c_page})
def signin(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        email=req.POST.get('email','')
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        cpassword=req.POST.get('cpassword','')
        if  password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,'username alredy exists')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'email alredy exists')
                return redirect('app:signin')
            else:
                user=User.objects.create_user(first_name=name,email=email,username=username,password=password)
                user.save()
                return redirect('app:login')
        else:
            messages.info(req,'password doesnt match')
            return redirect('app:signin')
    return render(req,'signin.html')
def login(req):
    if req.method=='POST':
        username=req.POST.get('username','')
        password=req.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect('app:home')
        else:
            messages.info(req,"inavalid details")
            return redirect('app:login')
    return render(req,'login.html')
def logout(req):
    auth.logout(req)
    return redirect('app:home')

def details(req,id):
    details=Product.objects.get(id=id)
    return render(req,'details.html',{"details":details})
