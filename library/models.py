from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    type=models.CharField(max_length=20)



class Books(models.Model):
    title=models.CharField(max_length=100)
    author=models.EmailField(max_length=100)
    isbn=models.CharField(max_length=10)
    category=models.CharField(max_length=20)
    status=models.CharField(default="Available")

class Checkouts(models.Model):
    member=models.CharField(max_length=200)
    book_title=models.TextField(null=True,blank=True)
    checkout_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    status=models.CharField(max_length=200,null=True,blank=True)