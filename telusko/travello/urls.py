from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index, name ='index'), # / for home or you can keep it empty.
]
  #when someone calls for the home page we need to handle it with a function.
    #in the home page we have a function called home.
    #name ='home' or you can use index.html  
