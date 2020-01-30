from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="tour"),
    path('token/', views.token, name="token"),
    path("checkout/", views.checkout, name="Checkout"),
    path('shopping/<int:myyid>', views.shopview, name="shopview"),


]
