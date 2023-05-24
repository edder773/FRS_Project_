from django.db import transaction
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serializers import DepositProductsSerializer, SavingProductsSerializer, DepositOptionsSerializer, SavingOptionSerializer
from .models import DepositProducts, SavingProducts, DepositOptions, SavingOptions
import requests
from accounts.models import User
from django.http import JsonResponse
import numpy as np
from django.db.models import Q

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

@api_view(['POST'])
def addproduct(request):
    user_id = request.data.get('user_id')
    product_id = request.data.get('product_id')

    user = User.objects.get(id=user_id)
    product = DepositProducts.objects.get(id=product_id)

    user.financial_products.add(product)  # 상품 가입

    return Response({"message": "상품 가입이 완료되었습니다."})


@api_view(['GET'])
def similar(request):
    # 현재 로그인된 사용자의 특성
    current_user = request.user
    current_age = current_user.age
    current_annual_income = current_user.annual_income
    current_assets = current_user.assets

    # 나이 범위 계산
    age_min = current_age - 7
    age_max = current_age + 7

    # 연수입 범위 계산
    income_min = current_annual_income - 10000000
    income_max = current_annual_income + 10000000

    # 자산 범위 계산
    assets_min = current_assets - 10000000
    assets_max = current_assets + 10000000

    # 비슷한 특성을 가진 사용자들의 financial_products 추출
    similar_users = User.objects.filter(
        Q(age__range=(age_min, age_max)) &
        Q(annual_income__range=(income_min, income_max)) &
        Q(assets__range=(assets_min, assets_max)) &
        ~Q(id=current_user.id)  # 현재 사용자는 제외
    )

    # 추천된 financial_products 리스트 추출
    recommended_products = []
    for user in similar_users:
        if user.financial_products:
            for i in user.financial_products.split(","):
                recommended_products.append(i)
    # 추천된 financial_products 리스트에서 중복 제거
    recommended_products = list(set(recommended_products))

    # 최대 10개의 추천된 financial_products 선택
    recommended_products = recommended_products[:10]

    # JSON 형태로 결과 반환
    data = {
        'recommended_products': recommended_products
    }
    return JsonResponse(data)
