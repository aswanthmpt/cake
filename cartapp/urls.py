from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    
     path('addcart/<int:id>',views.addcart,name='addcart'),
     path('diisplaycart/',views.displaycart,name='displaycart'),
     path('delete/<int:id>',views.delete,name='delete'),
  
]