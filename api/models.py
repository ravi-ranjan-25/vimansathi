from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cab.models import cabOrder

class airport(models.Model):
    name = models.CharField(unique=True,max_length=256)
    city = models.CharField(unique=False,max_length=256)
    state = models.CharField(unique=False,max_length=256)
    latitude = models.CharField(unique=False,max_length=256)
    longitude = models.CharField(unique=False,max_length=256)


    def __str__(self):
        return self.city

class airline(models.Model):
    name = models.CharField(unique=True,max_length=256)
    logo = models.CharField(unique=False,max_length=256)

    def __str__(self):
        return self.name

class routes(models.Model):
    flightid = models.CharField(unique=True,max_length=256)
    name = models.CharField(unique=False,max_length=256)
    origin = models.CharField(unique=False,max_length=256)
    destination = models.CharField(unique=False,max_length=256)
    Airline = models.ForeignKey(airline,on_delete = models.CASCADE)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    seat = models.IntegerField(unique=False,default=1,max_length=256)

    def __str__(self):
        return self.name

class days(models.Model):
    date = models.DateField()
    routeid = models.CharField(unique=False,default='ROUTE1',max_length=256)
    Route = models.ForeignKey(routes,on_delete = models.CASCADE)
    seat = models.IntegerField(unique=False,default=1,max_length=256)
    price = models.FloatField(max_length=256)

    def __str__(self):
        return self.Route.name

class book(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    dayobject = models.ForeignKey(days,on_delete = models.CASCADE)
    seat = models.IntegerField(unique=False,default=1,max_length=256)
    pnr = models.CharField(unique=True,max_length=256)
    amount = models.FloatField(max_length=256)
    risk = models.IntegerField(unique=False,default=0,max_length=256)

    def __str__(self):
        return self.pnr


class cat(models.Model):
    name = models.CharField(unique = False,default="NA",max_length=256)
    airport = models.CharField(unique=False,default="NA",max_length=256)
    store = models.BooleanField(default=False)
    restaurants = models.BooleanField(default=False)
    hotel = models.BooleanField(default=False)
    services = models.CharField(unique=False,default="NA",max_length=256)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    productName = models.CharField(unique = False,default="NA",max_length=256)
    productid = models.CharField(unique = True,default="NA",max_length=256)
    productDescription = models.CharField(unique = False,default="NA",max_length=256)
    stock = models.IntegerField(default=-1,max_length=256)
    active = models.BooleanField(default=True)
    display = models.CharField(unique=False,null=True,default="https://www.vikasanvesh.in/wp-content/themes/vaf/images/no-image-found-360x260.png",max_length=256)
    costPrice = models.FloatField(default=0.00,max_length=256)
    sellingPrice = models.FloatField(default=0.00,max_length=256)
    discount = models.FloatField(default=0.00,max_length=256)
    category = models.ForeignKey(cat,on_delete = models.CASCADE)
    total = models.IntegerField(default=1,max_length=256)
    rating = models.FloatField(default=1,max_length=256)

    def __str__(self):
        return self.productName


class order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='user')
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    amount = models.FloatField(default=0.00,max_length=256)
    orderid=models.CharField(unique = True,default="NA",max_length=256)
    quantity = models.IntegerField(unique=False,default=1,max_length=256)
    accept = models.IntegerField(unique=False,default=-1,max_length=256)
    delivery = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='deliver',default=None)
    selfpickup = models.BooleanField(default=True) 
    cab = models.ForeignKey(cabOrder,on_delete=models.CASCADE,null=True,default=None)
    time = models.DateTimeField(default = timezone.now())
    pickupDate = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.product.productName


class userdetails(models.Model):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mobile = models.CharField(unique = True,max_length=256)
    admin = models.BooleanField(default=False)
    objectname = models.CharField(unique = False,default="NA",max_length=256)
    resturants = models.BooleanField(default=False)
    airport = models.CharField(unique = False,default="NA",max_length=256)
    category = models.CharField(unique = False,default="NA",max_length=256)
    services = models.CharField(unique = False,default="NA",max_length=256)
    dp = models.CharField(unique = False,default="NA",max_length=256)
    doctor = models.BooleanField(default=False)
    latitude = models.CharField(null=True,default="0.00",max_length=256,unique=False)
    longitude = models.CharField(null=True,default="0.00",max_length=256,unique=False)
    time = models.DateTimeField(default = timezone.now())
    active = models.BooleanField(default=False)
    risk = models.IntegerField(default=0,max_length=10)
    serves = models.ForeignKey(cat,on_delete = models.CASCADE,null=True)
    deli = models.BooleanField(default=False)
    co =  models.ForeignKey(order,on_delete = models.CASCADE,null=True,default=None)
    total = models.IntegerField(default=1,max_length=256)
    rating = models.FloatField(default=1,max_length=256)
    cabIdle = models.BooleanField(default=True)
    cabO = models.ForeignKey(cabOrder,on_delete = models.CASCADE,null=True,default=None)

    def __str__(self):
        return self.user.username

# Create your models here.



class wallet(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    amount = models.FloatField(default=0.00,max_length=256)

    def __str__(self):
        return self.user.username

class hotel(models.Model):
    Order = models.ForeignKey(order,on_delete = models.CASCADE)
    checkin = models.CharField(unique = False,default="NA",max_length=256)
    checkout = models.CharField(unique = False,default="NA",max_length=256)
    Rating = models.FloatField(default=0.00,max_length=256)

    def __str__(self):
        return self.Order.orderid

class storerestro(models.Model):
    Order = models.ForeignKey(order,on_delete = models.CASCADE)
    preparing_packaging = models.BooleanField(default=False)
    dispatched = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    Rating = models.FloatField(default=0.00,max_length=256)
    time = models.DateTimeField(default = timezone.now())
    
    def __str__(self):
        return self.Order.orderid

class productComplain(models.Model):
    Order = models.ForeignKey(order,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    complainref = models.CharField(unique = True,default="NA",max_length=256)
    complain = models.CharField(unique = False,default="NA",max_length=256)
    status = models.IntegerField(default=-1,max_length=256)
    time = models.DateTimeField(default = timezone.now())
    





###################################################################################
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        
###################################################################################33        


class Doctor(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='patient')
    doctor = models.ForeignKey(User,on_delete = models.CASCADE,related_name='doctor')
    meet = models.BooleanField(default=False)
    chat = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    
    time = models.DateTimeField(default = timezone.now())
   

class Complain(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    complaintxn = models.CharField(max_length=256,default = "COMP123")
    complain = models.CharField(max_length=256)
    time = models.DateTimeField(default = timezone.now())
    complainid = models.CharField(max_length=256) 
    status = models.BooleanField(default=0)
    username = models.CharField(max_length=256,default="USER1")

    def __str__(self):
        return self.complain     


class Tax(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    Order = models.ForeignKey(order,on_delete = models.CASCADE,null=True)
    txnid = models.CharField(max_length = 256)
    credit = models.BooleanField(default=False)
    amount = models.FloatField(max_length=10)
    time = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.txnid


