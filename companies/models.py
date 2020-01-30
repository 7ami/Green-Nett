from django.db import models

# Create your models here.


class Accommo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    img = models.ImageField(upload_to="companies/images", default="")
    latitude = models.FloatField(default=27.71)
    longitude = models.FloatField(default=85.32)

    def __str__(self):
        return self.name


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    date = models.DateField()
    img = models.ImageField(upload_to="companies/images", default="")

    def __str__(self):
        return self.name


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    #price = models.IntegerField(default=0)
    desc = models.CharField(max_length=600)
    #date = models.DateField()
    img = models.ImageField(upload_to="companies/images/tour", default="")

    def __str__(self):
        return self.name


class Taxi(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=10)
    category = models.CharField(max_length=20, default="small")
    capacity = models.IntegerField(default=4)
    ratepm = models.IntegerField()
    phone = models.CharField(max_length=20)
    available = models.CharField(max_length=1)

    def __str__(self):
        return self.number


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc
