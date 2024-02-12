from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='categories',blank=True)
    desc=models.TextField(blank=True)
    
    class Meta:
            ordering=('name',)
            verbose_name='category'
            verbose_name_plural='categories'
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products',blank=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    weight=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return self.name
    
         
    