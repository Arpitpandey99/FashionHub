from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

from shopping.models import *
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponse


def all_category():
    all_cat = Category.objects.all()
    return all_cat

def Total(u):
    data = Add_to_cart.objects.filter(usr = u)
    total = 0
    for i in data:
        total += int(i.product.price)
    return total


def Home(request):
    products = Product.objects.all().order_by('-id')
    last_five = products[:5]
    sub_cat = Sub_category.objects.all().order_by('-id')
    subcat = sub_cat[:4]
    if request.user.is_authenticated():
        d = {'subcat':subcat,'last_five':last_five,'allcat' : all_category(),'total':Total(request.user)}
    else:
        d = {'last_five':last_five,'allcat':all_category()}
    return render(request, 'index.html',d)
def About(request):
    if request.user.is_authenticated():
        d = {'allcat' : all_category(),'total':Total(request.user)}
    else:
        d = {'allcat':all_category()}
    return render(request, 'about.html',d)

def Contact(request):
    if request.user.is_authenticated():
        d = {'allcat' : all_category(),'total':Total(request.user)}
    else:
        d = {'allcat':all_category()}
    return render(request, 'contact.html',d)

def products(request, cat_id):
    data = Sub_category.objects.filter(id = cat_id).first()
    if request.user.is_authenticated():
        d = {'allcat': all_category(),'subcat':data,'total':Total(request.user)}
    else:
        d = {'allcat': all_category(),'subcat':data,}
    return render(request,'products.html',d)

def product_details(request,p_id):
    pdata = Product.objects.filter(id = p_id).first()
    if request.user.is_authenticated():
        d = {'allcat': all_category(),'product':pdata,'total':Total(request.user)}
    else:
        d = {'allcat': all_category(),'product':pdata}

    return render(request,'product_details.html',d)

def Login(request):
    error = False
    if request.method == 'POST':
        u = request.POST['user']
        p = request.POST['pwd']
        us = authenticate(username = u ,password = p)
        if us:
            login(request,us)
            if request.user.is_staff:
                return redirect('admin_panel')
            else:
                return redirect('home')
        else:
            error = True
    d = {'allcat': all_category(),'error':error}
    return render(request,'login.html',d)

def AddToCart(request,pid):
    data = Product.objects.filter(id = pid).first()
    dd = Add_to_cart.objects.filter(product = data,usr = request.user)
    if dd:
        return redirect('mycart')
    else:

        Add_to_cart.objects.create(usr = request.user,product = data)
        return redirect('mycart')

def MyCart(request):
    total = 0
    mycart = Add_to_cart.objects.filter(usr=request.user)
    for i in mycart:
        total += int(i.product.price)
    d = {'allcat': all_category(), 'mycart': mycart,'total':Total(request.user)}
    return render(request ,'cart.html',d)

def Delete_item_from_cart(request,cid):
    data = Add_to_cart.objects.filter(id = cid).first()
    data.delete()
    return redirect('mycart')

def Signup(request):
    error = False
    if request.method == 'POST':
        u = request.POST['user']
        p = request.POST['pwd']
        n = request.POST['name']
        m = request.POST['mobile']
        e = request.POST['email']
        a = request.POST['address']
        user_data = User.objects.filter(username = u)

        if user_data:
            error = True
        else:
            user = User.objects.create_user(username = u ,password = p,first_name = n )
            User_detail.objects.create(user = user,name = n,mobile = m,email = e,address = a)
            return redirect('login')
    d = {'allcat': all_category(),'error' : error }
    return render(request,'signup.html',d)

def Order(request,pid):
    data = User_detail.objects.filter(user = request.user).first()
    address = data.address
    d = {'allcat': all_category(),'address' : address,'total':Total(request.user)}
    if request.method == 'POST':
        add = request.POST['address']
        product = Product.objects.filter(id = pid).first()
        data2 = Add_to_cart.objects.filter(product = product,usr = request.user)
        data2.delete()
        Order_placed.objects.create(user = request.user,product = product,address = add)
        sub = "Order placed"
        from_email = settings.EMAIL_HOST_USER
        d = {"name":data.name,"product":product.name,"price": product.price,"des": product.discription}
        html = get_template('mail.html').render(d)
        msg = EmailMultiAlternatives(sub,' ',from_email,[data.email])
        msg.attach_alternative(html,'text/html')
        #msg.send()
        return redirect('payment',pid)
    return render(request,'order.html',d)

def Clear_Cart(request):
    data = Add_to_cart.objects.filter(usr = request.user)
    data.delete()
    return redirect('home')

import requests
import json

headers = {"X-Api-Key": "36fedc81de23f05b7044ababd27d0555",
            "X-Auth-Token": "6fb6c5ad36a9baa8a7c734141a9535f3"}



def Admin_home(request):
    return render(request,'admin_home.html')

def AllCategory(request):
    data = Category.objects.all()
    d = {"allcat":data}
    return render(request,'allcat.html',d)

def Add_Category(request):
    if request.method == "POST":
        n = request.POST['cat']
        Category.objects.create(name = n)
        return redirect('all_cat')
    return render(request,'add_category.html')

def AllSubcategory(request):
    data = Sub_category.objects.all()
    d = {"allsubcat":data}
    return render(request,'allsubcat.html',d)

def Add_Subcategory(request):
    all_cat = Category.objects.all()
    d = {"allcat":all_cat}
    if request.method == "POST":
        c = request.POST['cid']
        cat = Category.objects.get(id = c)
        n = request.POST['subcat']
        Sub_category.objects.create(category = cat,name = n)
        return redirect('all_subcat')
    return render(request,'add_subcategory.html',d)

def AllProduct(request):
    data = Product.objects.all()
    d = {'all_product':data}
    return render(request,'allproduct.html',d)







