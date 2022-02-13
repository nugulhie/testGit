from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Product, User, Comment, Cart
from .serializers import UserSerializer, ProductSerializer, CommentSerializer, CartSerializer
from haversine import haversine

import requests
import datetime
import urllib.request
import json
import time

# Create your views here.
@api_view(['GET', 'POST'])
def productList(request, slug):
    try:
        productData = Product.objects
    except Product.DoesNotExist:
        print("asd")
        return JsonResponse({'success' : False, 'result' : {}}, status = status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET'):
        if slug == "0" :
            productSerializer = ProductSerializer(productData.all(), many = True)
            return JsonResponse({'success' : True, 'result' : productSerializer.data}, status = status.HTTP_200_OK,  json_dumps_params={'ensure_ascii': False})
        else:
            filteredData = productData.filter(productTitle = slug)
            if len(filteredData) == 0:
                return JsonResponse({'success' : False, 'result': {}}, status = status.HTTP_204_NO_CONTENT)
            else:
                productSerializer = ProductSerializer(filteredData, many = True)
                return JsonResponse({'success': True, 'result':productSerializer.data[0]}, status = status.HTTP_200_OK,  json_dumps_params={'ensure_ascii': False})
    if(request.method == 'POST'):
        parsedData = JSONParser().parse(request)
        parseSerializer = ProductSerializer(data = parsedData)
        if parseSerializer.is_valid():
            parseSerializer.save()
            return JsonResponse({'success':True, 'result':parseSerializer.data}, status = status.HTTP_201_CREATED)
        else:
            print(parseSerializer.errors)
            return JsonResponse({'success':False, 'result':{}}, status = status.HTTP_400_BAD_REQUEST)
