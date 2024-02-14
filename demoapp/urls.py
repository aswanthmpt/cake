from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    path('',views.home,name='home'),
     path('signin/',views.signin,name='signin'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     path('details/<int:id>',views.details,name='details'),
  
    path('prod_by_cat/<slug:c_slug>',views.home,name='prod_by_cat'),
   
]
