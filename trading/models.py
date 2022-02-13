from distutils.command.upload import upload
import email
from unicodedata import category
from django.db import models
from datetime import timezone
import os
import uuid

class User(models.Model): 
    '''DB column'''
    UID                     = models.BigAutoField(primary_key=True)
    #PID                     = models.ManyToManyField('Product')
    pwToekn                 = models.CharField(max_length=255, null=False)
    email                   = models.EmailField(max_length=100, null=False)
    name                    = models.CharField(max_length=50, null=False)
    address                 = models.CharField(max_length=100, null=False)
    phone                   = models.CharField(max_length=20, null=False)
    nickname                = models.CharField(max_length=10, null=False, default="ABC")

    def __str__(self):
        return self.nickname

class Product(models.Model):
    '''DB column'''
    PID                     = models.BigAutoField(primary_key=True)
    productTitle            = models.CharField(max_length=100, null=False)
    productDetail           = models.TextField(null=False)
    imageTitle              = models.TextField(null=True, default="a.jpg")
    imageFile               = models.ImageField(null=False)
    imageContext            = models.TextField(null=False, default="일반통행")
    # category                = models.ManyToManyField()

    def __str__(self):
        return self.productTitle

class Comment(models.Model):
    '''DB column'''
    id                      = models.BigAutoField(primary_key=True)
    nickname                = models.CharField(max_length=10, null=False, default="ABC")
    comment                 = models.TextField(null=False)

    def __str__(self):
        return self.id

class Cart(models.Model): 
    '''DB column'''
    CID                     = models.BigAutoField(primary_key=True)
    #UID                     = models.ForeignKey()

    def __str__(self):
        return self.CID