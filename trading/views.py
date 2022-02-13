from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .models import Product, User, Comment, Cart
from .serializers import UserSerializer, ProductSerializer, CommentSerializer, CartSerializer
import requests
import datetime
import urllib.request
import json

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def productList(request):
    try:
        productData = Product.object
    except Product.DoesNotExist:
        return JsonResponse({'success' : False, 'result' : {}}, status = status.HTTP_404_NOT_FOUND)

    if(request.method == 'GET')