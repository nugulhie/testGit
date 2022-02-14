from django.db.models import fields
from rest_framework import serializers
from .models import User, Product, Comment, Cart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UID', 'pwToekn', 'email', 'name', 'address', 'phone', 'nickname', 'pushToken']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['PID', 'productTitle', 'productDetail', 'imageTitle', 'imageFile', 'imageContext']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'nickname', 'comment']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart 
        fields = ['CID', 'UID']