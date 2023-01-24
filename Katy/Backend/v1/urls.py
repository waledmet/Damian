
from django.urls import path, include  
from v1.views import *
urlpatterns = [
    path('v1/create_customer/',create_customer, name="create_customer"),           
    path('v1/quote/',create_quote, name="create_quote"),           
   

]