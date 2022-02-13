import email
from unicodedata import category
from django.db import models

class User(models.Model): 
    '''DB column'''
    UID                     = models.BigAutoField(primary_key=True)
    #PID                     = models.ManyToManyField('Product')
    pwToekn                 = models.CharField(max_length=255)
    email                   = models.EmailField(max_length=100)
    name                    = models.CharField(max_length=50)
    address                 = models.CharField(max_length=100)
    phone                   = models.CharField(max_length=20)
    nickname                = models.CharField(max_length=10)

    def __str__(self):
        return self.nickname

class Product(models.Model):
    '''DB column'''
    PID                     = models.BigAutoField(primary_key=True)
    productTitle            = models.CharField(max_length=100)
    productDetail           = models.TextField()
    category                = models.ManyToManyField()

    def __str__(self):
        return self.productTitle

class Comment(models.Model):
    '''DB column'''
    id                      = models.BigAutoField(primary_key=True)    
    nickname                = models.CharField(max_length=10)
    comment                 = models.TextField()

    def __str__(self):
        return self.UID

class Cart(models.Model): 
    '''DB column'''
    CID                     = models.BigAutoField(primary_key=True)
    UID                     = models.ForeignKey()    

    def __str__(self):
        return 