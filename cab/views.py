from django.shortcuts import render
from api.models import userdetails,Product,wallet,order,hotel,storerestro,Doctor,Complain,Tax,cat,airport,airline,routes,days,book
from cab.models import carClass,cabdetails,cabOrder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse
import random
# from .serializers import ,UserSerializer,participateSerializer,EventSerializer,userDetailsSerializer
from rest_framework.generics import ListAPIView
from api.serializers import orderSerializer,userdetailsSerializer,bookSerializer
from .serializers import carClassSerializer,cabdetailsSerializer,cabOrderSerializer,kafkaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime
import time
from confluent_kafka import Producer, Consumer
import random
import json
import uuid




# import s2geometry as s2
def createmyuser(request):
    u = User.objects.create_superuser('ravi1','ravi2514999@myemail.com','maverick')
    u.save()
    return JsonResponse({'result':2})


def addcab(request):
    Username = request.GET.get('username')
    model = request.GET.get('carmodel')
    Registration = request.GET.get('carregistration')
    color = request.GET.get('carcolor')
    Type = int(request.GET.get('type'))

    

    typeArr = ['SEDAN','AUTO','BIKE','MINI']

    t = typeArr[Type]

    c = carClass.objects.get(cartype=t)
    user1 = User.objects.get(username=Username)
    ca = cabdetails(user=user1,cartype=c,carModel=model,carRegistration=Registration.upper(),carColor=color)
    ca.save()

    return JsonResponse({'result':1})

def gettxnid():
    txnid1 = random.randint(100,999) + random.randint(9999,10000) 

    txn = "TXN15"+str(txnid1)
    
    return txn

def caborder(request):
    Username = request.GET.get('username')
    latorigin = request.GET.get('latitudeorigin')
    longorigin = request.GET.get('longitudeorigin')
    latdestination = request.GET.get('latitudedestination')
    longdestination = request.GET.get('longitudedestination')
    Origin = request.GET.get('origin')
    Destination = request.GET.get('destination')
    Seat = request.GET.get('seat')
    Price = request.GET.get('price')
    Type = int(request.GET.get('type'))
    pl = request.GET.get('picklater')
    
    if pl is not None:
        pl=datetime.datetime.strptime(pl, '%Y-%m-%d %H:%M:%S')
    else:
        pl = timezone.now()

    typeArr = ['SEDAN','AUTO','BIKE','MINI']

    t = typeArr[Type]

    c = carClass.objects.get(cartype=t)
    

    user1 = User.objects.get(username=Username)
    user2 = User.objects.get(username='admin')
    cid = 'CAB'+str(random.randint(9999,99999))    
    c = cabOrder(cartype=c,cabid=cid,user=user1,origin=Origin.upper(),destination=Destination.upper,latitudeOrigin=latorigin,longitudeOrigin=longorigin,latitudeDestination=latdestination,longitudeDestination=longdestination,seat=Seat,price=Price,pickupTime=pl)

    c.save()

    w1 = wallet.objects.get(user = user1)
    w2 = wallet.objects.get(user__username = 'admin')

    w1.amount = w1.amount - 0.2*float(c.price) + float(c.price)
    w2.amount = w2.amount + 0.2*float(c.price)

    txn = gettxnid()
    
    t = Tax(user = user1,Order=None,txnid=txn,credit=True,amount=float(c.price))
    t.save()

    txn = gettxnid()
    
    t = Tax(user = user2,Order=None,txnid=txn,credit=True,amount=0.2*float(c.price))
    t.save()


    return JsonResponse({'cab':cid})

def cabidorder(request):
    cid = request.GET.get('cabid')
    co = cabOrder.objects.get(cabid=cid)

    serial = cabOrderSerializer(co)

    return JsonResponse({'result':serial.data})

def accept(request):
    cid = request.GET.get('cabid')
    Username = request.GET.get('username')
    
    c = cabdetails.objects.get(user__username=Username)
    co = cabOrder.objects.get(cabid=cid)
    co.cab = c
    co.accept=0
    co.save()



    return JsonResponse({'result':1})

def scanqr(request):
    cid = request.GET.get('cabid')
    
    co = cabOrder.objects.get(cabid=cid)
    co.accept=1
    co.save()
    
    
    
    serial = cabOrderSerializer(co)
    return JsonResponse({'details':serial.data})

def completeride(request):
    cid = request.GET.get('cabid')
    
    co = cabOrder.objects.get(cabid=cid)
    co.accept=2
    co.cab.totalRides += 1
    co.cab.save()
    co.save()

    w = wallet.objects.get(user=co.cab.user)
    w.amount = w.amount + 0.8*co.price
    w.save()
    txn = gettxnid()
    
    t = Tax(user = co.cab.user,Order=None,txnid=txn,credit=True,amount=0.8*co.price)
    t.save()

    return JsonResponse({'result':1})

def showavailablerides(request):
    lat = request.GET.get('latitude')
    longi = request.GET.get('longitude')
    Username = request.GET.get('username')
    # S2 Library
    c = cabdetails.objects.get(user__username=Username)
    co = cabOrder.objects.filter(cab=None,cartype=c.cartype)
    list = []
    for c in co:
        serial = cabOrderSerializer(c)
        list.append({'User FirstName':serial.data['user']['first_name'],'cabid':serial.data['cabid'],'latitude':serial.data['latitudeOrigin'],'longitude':serial.data['longitudeOrigin']})

    return JsonResponse({'result':list})

def addRating(request):
    cid = request.GET.get('cabid')
    Rating = float(request.GET.get('rating'))
    
    co = cabOrder.objects.get(cabid=cid)
    
    co.rating = Rating
    co.cab.rating = ((co.cab.totalRides * co.cab.rating) + Rating)/co.cab.totalRides
    co.save()

    return JsonResponse({'result':co.cab.rating})


def kafkaProduce(request):
    Username = request.GET.get('username')
    Latitude = request.GET.get('latitude')
    Longitude = request.GET.get('longitude')


    producer = Producer({
    'bootstrap.servers': 'pkc-l7pr2.ap-south-1.aws.confluent.cloud:9092',
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': '7AQPX7D57YCZZYFV',
    'sasl.password': '9De6dmWhaYomN26JULSABceMmAoeI6Ln5PCeQmTRYjv8SjXLwNczMVFplre3okw3'
    })

    data = {}
    data['id'] = str(random.randint(9999,99999))
    data['username'] = Username
    data['latitude'] = float(Latitude)
    data['longitude'] = float(Longitude)
    data['key'] = str(random.randint(9999,99999))
    
    message = json.dumps(data)
    future = producer.produce('cab',key=data['key'].encode('utf-8'),value=message.encode('utf-8'))

    producer.flush()

    return JsonResponse({'result':1})          


def consume(request):
    Username = request.GET.get('username')


    c = Consumer({
        'bootstrap.servers': 'pkc-l7pr2.ap-south-1.aws.confluent.cloud:9092',
        'sasl.mechanism': 'PLAIN',
        'security.protocol': 'SASL_SSL',
        'sasl.username': '7AQPX7D57YCZZYFV',
        'sasl.password': '9De6dmWhaYomN26JULSABceMmAoeI6Ln5PCeQmTRYjv8SjXLwNczMVFplre3okw3',
        'group.id': str(uuid.uuid1()),  
        'auto.offset.reset': 'latest'
    })

    c.subscribe(['cab'])
    list = []


    def results(count):
        while count:
            msg = c.poll(0.4)
            
            if msg is None:
                continue
            if msg.error():
                continue
        
            m = msg.value().decode('ascii')
            
            z = json.loads(m)
            if z['username'] == Username:
                list.append(z)
                count -= 1
            

    results(1)
    return JsonResponse({'result':list})          
    # def events():
    #     try:
    #         while True:
    #             msg = c.poll(0.1)  # Wait for message or event/error
    #             if msg is None:
    #                 # No message available within timeout.
    #                 # Initial message consumption may take up to `session.timeout.ms` for
    #                 #   the group to rebalance and start consuming.
    #                 continue
    #             if msg.error():
    #                 # Errors are typically temporary, print error and continue.
    #                 print("Consumer error: {}".format(msg.error()))
    #                 continue
    #             m = msg.value()    
    #             yield msg.value()

    #         return Response({'result':events},mimetype)
            
        
    # except KeyboardInterrupt:
    #     pass

    # finally:
    #     # Leave group and commit final offsets
    #     c.close()

def activeFlightordersByCity(user1,Airport,Date):
    
    a = airport.objects.get(name=Airport.upper())

    getBooking = book.objects.filter(user__username=user1,dayobject__date=Date,dayobject__Route__destination=a.city)
    print(Date)
    list = []
    for i in getBooking:
        serial = bookSerializer(i)
        list.append(serial.data)

    # return JsonResponse({'flight':list})
    
    return list    


def storerestroordersbycity(user1,code,Date):
  
    list = []
    
    o = order.objects.filter(user__username=user1,pickupDate__day=Date.day,pickupDate__month=Date.month,pickupDate__year=Date.year).exclude(accept=3)
    
    for i in o:
        ud = userdetails.objects.get(user=i.product.user)
        if ud.airport == code.upper():
            if ud.category == 'STORE' or ud.category=='RESTUARANTS':
                serial = orderSerializer(i)
                list.append(serial.data)
            

    # return JsonResponse({'storerestro':list})
    # print(list)
    return list    


def droploactionsuggestion(user1,code,Date):
  
    list = []
    o = order.objects.filter(user__username=user1)
    
    for i in o:
        ud = userdetails.objects.get(user=i.product.user)
        if ud.airport == code.upper():
            if ud.category == 'HOTEL':
                ho = hotel.objects.get(Order=i)
                Date1=datetime.datetime.strptime(ho.checkin, '%Y-%m-%d %H:%M:%S.%f')
                if Date.day == Date1.day and Date.month == Date1.month and Date.year == Date1.year:
                    serial = orderSerializer(i)
                    serialud = userdetailsSerializer(ud)

                list.append({'hotel order':serial.data,'details':serialud.data})
            

    return list    

def masterfunc(request):
    Username = request.GET.get('username')
    Airport = request.GET.get('airport')
    Date = request.GET.get('date')

    list1 = activeFlightordersByCity(Username,Airport,Date)    

    Date=datetime.datetime.strptime(Date, '%Y-%m-%d')

    Date = Date.date()

    
    list2 = storerestroordersbycity(Username,Airport,Date)

    list3 = droploactionsuggestion(Username,Airport,Date)

    return JsonResponse({'Sync Time':list1,'Sync delivery':list2,'Sync drop location':list3})

def changepickuptime(request):
    cid = request.GET.get('cabid')
    c = cabOrder.objects.get(cabid=cid)
    o = request.GET.get('pnr')
    pickLater = request.GET.get('picklater')
   
    if pickLater is None:
        
        od = book.objects.get(pnr=o)
        Date = od.dayobject.date
        Time = od.dayobject.Route.arrival
        nt = datetime.datetime.combine(Date,Time.time())


        c.pickupTime = nt
        c.save()

    return JsonResponse({'result':1})


def addCab(request):
    cid = request.GET.get('cabid')
    o = request.GET.get('orderid')


    c = cabOrder.objects.get(cabid=cid)
    od = order.objects.get(orderid=o)
    od.selfpickup = False

    od.cab = c

    od.save()

    return JsonResponse({'result':1})


def adddropLocation(request):
    cid = request.GET.get('cabid')
    o = request.GET.get('orderid')


    c = cabOrder.objects.get(cabid=cid)
    od = order.objects.get(orderid=o)
    ud = userdetails.objects.get(user=od.user)
    c.latitudeDestination = ud.latitude
    c.longitudeDestination = ud.longitude

    c.save()

    return JsonResponse({'result':1})