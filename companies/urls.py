from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour, name="tour"),
    #path('tour/', views.tour, name="tour"),
    path('tours/<int:myid>', views.tourview, name="tourview"),
    path('guide/', views.guide, name="guide"),
    path('dinn/', views.dinning, name="dinning"),
    path('token/', views.token, name="token"),
    path('aptaxi/', views.aptaxi, name="aptaxi"),
    path('accommo/', views.accommo, name="accommo"),
    path("checkout/", views.checkout, name="Checkout"),
    path('hotels/<int:myid>', views.hotelview, name="hotelview"),
    path('shopping/<int:myyid>', views.shopview, name="shopview"),
    path('ticket/', views.ticket, name="ticket"),


]
