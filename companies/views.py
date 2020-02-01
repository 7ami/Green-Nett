from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Token, Orders, OrderUpdate, Contact
from math import ceil
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
# Create your views here.


def token(request):
    includeall = []
    prodscat = Token.objects.values('category', 'id')
    maincat = {item['category'] for item in prodscat}
    print('amir')
    for c in maincat:
        ingri = Token.objects.filter(category=c)
        num = len(ingri)
        nsli = num // 4 + ceil((num / 4) - (num // 4))
        includeall.append([ingri, range(1, nsli), nsli])
    parameters = {'proall': includeall}
    return render(request, 'companies/token.html', parameters)


def home(request):
    return render(request, 'companies/home.html')
 # django automatically takes id iff nott mentioned primary key


def shopview(request, myyid):
    fashion = Token.objects.filter(id=myyid)
    return render(request, 'companies/shopview.html', {'product': fashion[0]})


def checkout(request):
    hell = False
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + \
            " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       phone=phone, amount=amount)
        order.save()
        hell = True
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        update.save()
    return render(request, 'companies/checkout.html', {'hello': hell})
    # '''# Request paytm to transfer the amount to your account after payment by user
    # )
    # return render(request, 'shop/checkout.html')'''


def loginhandle(request):

    if request.method == "POST":
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass1")
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)
            # print(uname, pass1)
            return redirect("token")
        else:
            messages.error(request, "Invalid,please try again")
            # print(uname, pass1)

    return render(request, "companies/login.html")




def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        mess = request.POST.get('mess', '')
        print(name, email, phone, mess)
        contact = Contact(name=name, email=email, phone=phone, mess=mess)
        contact.save()
        thank = True
    return render(request, 'companies/contact.html', {'thank': thank})


def about(request):
    return render(request, 'companies/about.html')
