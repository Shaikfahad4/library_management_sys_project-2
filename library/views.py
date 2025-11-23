from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
import json
from .models import *

# Create your views here.
from .models import *
@login_required(login_url="/loginview/")
def retriving_data_book(request):
    checkout_title=Checkouts.objects.values_list("book_title",flat=True)
    books=Books.objects.all()
    books_list=[]
    for i in books:
         books_list.append({
              "id":i.id,
              "title":i.title,
              "author":i.author,
              "isbn":i.isbn,
              "category":i.category,
              "status":"Checkout" if i.title in checkout_title else "Available"
         })
         
              
    context={"books":books_list}
    return render(request,"books.html",context)

def user_inserting_book(request):
    if request.method=="POST":
         title=request.POST.get("title"),
         author=request.POST.get("author"),
         isbn=request.POST.get("isbn"),
         category=request.POST.get("category")
         if not title or not author or not isbn or not category:
              messages.info(request,"Please the all details")
              return redirect(retriving_data_book)
         else:
            Books.objects.create(
                title=request.POST.get("title"),
                author=request.POST.get("author"),
                isbn=request.POST.get("isbn"),
                category=request.POST.get("category")
            )
            messages.success(request,"Book Enetred")
            
    return redirect(retriving_data_book)


def retriving_data_member(request):
    members=list(Member.objects.all().values())
    context={"members":members}
    return render(request,"member.html",context)

def user_inserting_member(request):
    if request.method=="POST":
         name=request.POST.get("name")
         email=request.POST.get("email")
         phone=request.POST.get("phone")
         type=request.POST.get("type")
         if not name or not email or not phone or not type:
            messages.info(request,"Please the all details")
            return redirect(retriving_data_member)
         else:
            Member.objects.create(
                name=name,
                email=email,
                phone=phone,
                type=type)
            messages.success(request,"Book Enetred")
    return redirect(retriving_data_member)

def checkoutdata(request):
    checkout_title=Checkouts.objects.values_list("book_title",flat=True)
    books=Books.objects.all()
    books_list=[]
    for i in books:
         books_list.append({
              "id":i.id,
              "title":i.title,
              "author":i.author,
              "isbn":i.isbn,
              "category":i.category,
              "status":"Checkout" if i.title in checkout_title else "Available"
         })
    member=list(Member.objects.all().values())
    checkout_list=list(Checkouts.objects.all().values())
    context={"books":books_list,"member":member,"checkout_list":checkout_list}
    return render(request,"checkout.html",context)

def user_inserting_checkout(request):
        if request.method=="POST":
            member=request.POST.get("memberName")
            book_title=request.POST.get("Bookname")
            due_date_1=request.POST.get("duedate")
            if not member or not book_title or not due_date_1:
                 messages.info(request,"PLease enter all required data")
                 return redirect("checkoutdata")
            due_date_str=datetime.strptime(due_date_1,"%m/%d/%Y").date()
            today=date.today()
            checkout_status="Overdue" if today>due_date_str else "Active"
            Checkouts.objects.create(
                member=member,
                book_title=book_title,
                due_date=due_date_str,
                status=checkout_status
                
            )
            messages.success(request,"checkout added successfully")
        return redirect(checkoutdata)

def delete_return(request,id):
    checkout_item=Checkouts.objects.get(id=id)
    checkout_item.delete()
    return redirect(checkoutdata)



    
def reports(request):
    checkout_title=Checkouts.objects.values_list("book_title",flat=True)
    books=Books.objects.all()
    books_list=[]
    for i in books:
         books_list.append({
              "id":i.id,
              "title":i.title,
              "author":i.author,
              "isbn":i.isbn,
              "category":i.category,
              "status":"Checkout" if i.title in checkout_title else "Available"
         })
    Total_Books=books.count()
    Available_books = Books.objects.exclude(title__in=checkout_title).count()
    checkout_books = Checkouts.objects.filter(status="Active").count()
    checkouts=Checkouts.objects.all().count()
    total_member=Member.objects.all().count()
    Overdue_books = Checkouts.objects.filter(due_date__lt=date.today()).count()
         
    context={
         "Total_Books":Total_Books,
         "Available_books":Available_books,
         "checkout_books":checkout_books,
         "total_member":total_member,
         "Overdue_books":Overdue_books
    }
    return render(request,"reports.html",context)
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("user_name")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request,"invalid username")
            return redirect(login_page)
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"invalid Password")
            return redirect(login_page)
        else:
            login(request,user)
            return redirect("/bookview/")
         
    return render(request,"login.html")
def logout_page(request):
     logout(request)
     return redirect(login_page)
def register(request):
     if request.method=="POST":
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            username=request.POST.get("user_name")
            password=request.POST.get("password")

            user=User.objects.filter(username=username)
            if user.exists():
                 messages.info(request,"Username Already exists")
                 return redirect(register)
            

            user=User.objects.create_user(
                 first_name=first_name,
                 last_name=last_name,
                 username=username
            )
            user.set_password(password)
            user.save()
            messages.info(request,"username created successfully")
            return redirect(register)
     return render(request,"register.html")



