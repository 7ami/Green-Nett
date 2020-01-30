from django.shortcuts import render, HttpResponse
from .models import Accommo, Token, Tour,Taxi,Orders,OrderUpdate
from math import ceil
import json
# Create your views here.


def accommo(request):
    everyprod = []
    catprods = Accommo.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prods = Accommo.objects.filter(category=cat)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        everyprod.append([prods, range(1, nSlides), nSlides])

    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # everyprod = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allProds': everyprod}
    return render(request, 'companies/accommo.html', params)


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


def hotelview(request, myid):
    product = Accommo.objects.filter(id=myid)
    return render(request, 'companies/hotelview.html', {'product': product[0]})

def shopview(request, myyid):
    fashion = Token.objects.filter(id=myyid)
    return render(request, 'companies/shopview.html', {'product': fashion[0]})


def tour(request):
    '''everyprodtour = []
    catprods = Tour.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prods = Tour.objects.filter(category=cat)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        everyprodtour.append([prods, range(1, nSlides), nSlides])
    paramet = {'everyprodtour': everyprodtour}'''
    return render(request, 'companies/asterik.html')

def tourview(request, myid):
    place = Tour.objects.filter(id=myid)
    return render(request, 'companies/tourview.html', {'place': place[0]})


def aptaxi(request):
    everyprod = []
    cattaxis = Taxi.objects.values('category', 'id')
    cats = {item['category'] for item in cattaxis}
    for cat in cats:
        taxis= Taxi.objects.filter(category=cat)
        n = len(taxis)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        everyprod.append([taxis, range(1, nSlides), nSlides])
    params = {'allTaxis': everyprod}
    return render(request, 'companies/aptaxi.html',params)



def dinning(request):
    return render(request, 'companies/dinning.html')


def ticket(request):
    return render(request, 'companies/ticket.html')

# dummy data for test
guides=[{'img':' ','name':"guidename",'description':"fsdkfjhsdjkfhjsk fsd fs fsdfsdfsdfs fsdfsdf",'detail':"detail1"},{'name':"guidename",'description':"sadasdsasfhjsk fsd fs fsdfsdfsdfs fsdfsdf",'detail':"detail1"},{'name':"guidename",'description':"mbnmbnmbjkfhjsk fsd fs fsdfsdfsdfs fsdfsdf",'detail':"detail3"},{'img':' ','name':"guidename",'description':"fsdkfjhsdjkfhjsk fsd fs fsdfsdfsdfs fsdfsdf",'detail':"detail1"},{'name':"guidename",'description':"sadasdsasfhjsk fsd fs fsdfsdfsdfs fsdfsdf",'detail':"detail1"},{'name':"guidename",'description':"mbnmbnmbjkfhjsk fsd fs fsdfsdfsdfs fsdfsdf",'detail':"detail3"}]

def guide(request):
    context={'guides':guides}
    return render(request, 'companies/guide.html',context)




def checkout(request):
    hell = False
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
        phone=phone, amount=amount)
        order.save()
        hell=True
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
    return render(request, 'companies/checkout.html', {'hello':hell})
        #'''# Request paytm to transfer the amount to your account after payment by user
      # )
       # return render(request, 'shop/checkout.html')'''

