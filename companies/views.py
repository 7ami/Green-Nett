from django.shortcuts import render, HttpResponse
from .models import Token, Orders, OrderUpdate
from math import ceil
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
