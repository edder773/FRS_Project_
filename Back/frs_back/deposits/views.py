from django.db import transaction
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import DepositProductsSerializer, SavingProductsSerializer, DepositOptionsSerializer, SavingOptionSerializer
from .models import DepositProducts, SavingProducts, DepositOptions, SavingOptions
import requests
API_KEY = settings.API_KEY

# Create your views here.
@api_view(['GET'])
def products(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }
    with transaction.atomic():
        DepositProducts.objects.all().delete()
        DepositOptions.objects.all().delete()
    
    response = requests.get(url, params=params)
    products_data = response.json()['result']['baseList']
    
    for i, product_data in enumerate(products_data):
        product_serializer = DepositProductsSerializer(data=product_data)
        product_data['id'] = i + 1
        if product_serializer.is_valid():
            product = product_serializer.save()
        options_data = response.json()['result']['optionList']
        for j, option_data in enumerate(options_data):
            if option_data['fin_prdt_cd'] == product_data['fin_prdt_cd']:
                option_data['fin_prdt_cd'] = product.id
            option_serializer = DepositOptionsSerializer(data=option_data)
            if option_serializer.is_valid():
                option_serializer.save()
            # print(option_serializer.errors)
    serialized_data = DepositProductsSerializer(DepositProducts.objects.all(), many=True).data
    
    return Response(serialized_data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def savings(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }
    
    with transaction.atomic():
        SavingProducts.objects.all().delete()
        SavingOptions.objects.all().delete()
        
    response = requests.get(url, params=params)
    savings_data = response.json()['result']['baseList']
    # return Response(products_data)
    for i, saving_data in enumerate(savings_data):
        saving_serializer = SavingProductsSerializer(data=saving_data)
        saving_data['id'] = i + 1
        if saving_serializer.is_valid():
            saving = saving_serializer.save()
        options_data = response.json()['result']['optionList']
        for option_data in options_data:
            if option_data['fin_prdt_cd'] == saving_data['fin_prdt_cd']:
                option_data['fin_prdt_cd'] = saving.id
            option_serializer = SavingOptionSerializer(data=option_data)
            if option_serializer.is_valid():
                option_serializer.save()
    serialized_data = SavingProductsSerializer(SavingProducts.objects.all(), many=True).data
    return Response(serialized_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def products_option(request):
    deposit_options = DepositOptions.objects.all()
    serialized_data = DepositOptionsSerializer(deposit_options, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def savings_option(request):
    saving_options = SavingOptions.objects.all()
    serialized_data = SavingOptionSerializer(saving_options, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)