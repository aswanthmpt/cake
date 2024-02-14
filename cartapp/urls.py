from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    
     path('cart/<int:id>',views.cart,name='cart'),
  
]