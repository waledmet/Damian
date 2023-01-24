from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from v1.serializers import CustomerSerializer,  QuoteSerializer
from v1.models import customer
from datetime import datetime
# Create your views here.


@api_view(['Post'])
def create_customer(request):
    user_id=0
    mutable = request.POST._mutable
    request.POST._mutable=True
    request.data['create_id'] = user_id
    dob=request.data['dob']
    if dob!="":request.data['dob']=datetime.strptime(dob, '%d/%m/%Y')
    request.POST._mutable=mutable
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        customer = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Post'])
def create_quote(request):
    user_id=0
    mutable = request.POST._mutable
    request.POST._mutable=True
    request.data['create_id'] = user_id
    #customer_id=request.data['customer_id']
    
    #request.data["customer"]=customer.objects.filter(id=customer_id).first()
    request.POST._mutable=mutable
    serializer = QuoteSerializer(data=request.data)
    if serializer.is_valid():
        quote = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    