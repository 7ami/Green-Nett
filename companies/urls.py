from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="tour"),
    path('token/', views.token, name="token"),
    path("checkout/", views.checkout, name="Checkout"),
    path('contact/', views.contact, name="ContactUs"),
    path('about/', views.about, name="about"),
    path('shopping/<int:myyid>', views.shopview, name="shopview"),


]
