from django.shortcuts import render
from api.models import userdetails,Product,wallet,order,hotel,storerestro,Doctor,Complain,Tax,cat,airport
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.http import JsonResponse
import random
# from .serializers import eventSerializer,UserSerializer,participateSerializer,EventSerializer,userDetailsSerializer
from rest_framework.generics import ListAPIView
from .serializers import ProductSerializer,orderSerializer,userdetailsSerializer,UserSerializer,complainSerializer,transactionSerializer,catSerializer,hotelSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


# Create your views here.
def signup(request):
    userName = request.GET.get('username')
    eMail = request.GET.get('email')
    firstname = request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    Password = request.GET.get('password')
    Mobile = request.GET.get('mobile')
    Airport = request.GET.get('airport')
    Category1 = request.GET.get('category')
    Object_name = request.GET.get('object_name')
    service = request.GET.get('services')
    D=request.GET.get('doctor')
    lat = request.GET.get('latitude')
    longi = request.GET.get('longitude')


    check = User.objects.filter(username = userName)
    checkEmail = User.objects.filter(email = eMail)
    checkHouse = userdetails.objects.filter(mobile=Mobile)
   

    if len(check) > 0:
        
            return JsonResponse({'result':0,'message':'Username already exist'})
    
    elif len(checkEmail) > 0:

            return JsonResponse({'result':0,'message':'Email address already exist'})


    elif len(checkHouse) > 0:
             return JsonResponse({'result':0,'message':'Mobile already registered'}) 

    
    else:
        # if Cab == 'y':
        #     Cab = True
        # else:
        #     Cab = False
        
        # if Hotel == 'y':
        #     Hotel = True
        # else:
        #     Hotel = False

        # if Restro == 'y':
        #     Restro = True
        # else:
        #     Restro = False

        # if Store == 'y':
        #     Store = True
        # else:
        #     Store = False    

        if Category1 is not None:
            Category1 = Category1.upper()
            
        else:
            Category1 = 'NA'

        if Object_name is None:
            Object_name = 'NA'

        if Airport is None:
            Airport = 'NA'

        if service is None:
            service = None
        else:
            if Category1 == 'STORE':
                c = cat.objects.filter(name=service.upper(),store=True)
                if len(c) > 0:
                    service=c[0]
                else:
                    z = cat(name=service.upper(),airport=Airport,store=True) 
                    z.save()
                    service=z   

            elif Category1 == 'RESTAURANTS':
                c = cat.objects.filter(name=service.upper(),restaurants=True)
                if len(c) > 0:
                    service=c[0]
                else:
                    z = cat(name=service.upper(),airport=Airport,restaurants=True) 
                    z.save()
                    service=z   
            
            elif Category1 == 'HOTEL':
                c = cat.objects.filter(name=service.upper(),hotel=True)
                if len(c) > 0:
                    service=c[0]
                else:
                    z = cat(name=service.upper(),airport=Airport,hotel=True) 
                    z.save()
                    service=z   
        


        if D is not None:
            D = True
        else:
            D = False

        if longi is None:
            longi = '0.0'
        if lat is None:
            lat = '0.0'

        user1 = User.objects.create_user(username = userName, email=eMail, password=Password, first_name = firstname , last_name = lastname)
        userD = userdetails(user=user1,mobile=Mobile,resturants=False,category=Category1,airport=Airport,objectname=Object_name,serves=service,doctor=D,longitude=longi,latitude=lat)

        w = wallet(user=user1)
        w.save()
        user1.save()
        userD.save()
        return JsonResponse({'result':1,'message':'success'})

def getWallet(request):
    Username = request.GET.get('username')

    w = wallet.objects.get(user__username=Username)

    return JsonResponse({'wallet':w.amount})


def staticimg(request):
    Username = request.GET.get('username')
    D = request.GET.get('dp')

    ud = userdetails.objects.get(user__username=Username)
    
    ud.dp=D
    ud.save()
    return JsonResponse({'result':1,'message':'success'})



def login(request):
    userName = request.GET.get('username')
    Password = request.GET.get('password')
    

    user1 = authenticate(username=userName, password=Password)
    
    if user1 is not None:
        house = userdetails.objects.get(user = user1)
        return JsonResponse({'result':1,'username':user1.username,'email':user1.email,'firstname':user1.first_name,
                                'lastname':user1.last_name,'mobile':house.mobile,'objectName':house.objectname,
                                'address':house.airport,'category':house.category,'airport':house.airport,'latitude':house.latitude,'longitude':house.longitude})
    
    else:
        return JsonResponse({'result':0,'message':'Incorrect username or password'})


def addProduct(request):
    Username = request.GET.get('username')
    Name = request.GET.get('name')
    Description = request.GET.get('description')
    Stock = request.GET.get('stock')
    Active = request.GET.get('active')
    Display = request.GET.get('dp')
    cost = request.GET.get('costprice')
    sell = request.GET.get('sellprice')
    Discount= request.GET.get('discount')
    service = request.GET.get('category')

    if Active == 'y':
        Active = True
    else:
        Active = False    


    ud = userdetails.objects.get(user__username=Username)
    

    c = cat.objects.filter(name=service.upper())
    if len(c) > 0:
        
        if ud.airport == c[0].airport:
            service=c[0]

    else:
        Airport = ud.airport
        z = cat(name=service.upper(),airport=Airport) 
        z.save()
        service=z   
            
    print(service)
    user1 = User.objects.get(username=Username)
    # userD = userdetails.object.get(user = user1)
    proid = "PROD"+str(random.randint(9999,99999))
    add = Product(user=user1,productName=Name,productid=proid,productDescription=Description,stock=Stock,active=Active,display=Display,costPrice=cost,sellingPrice=sell,discount=Discount,category=service)
    add.save()



    return JsonResponse({'result':1,'message':'Success'})

def editproduct(request):
    Name = request.GET.get('Name')
    Description = request.GET.get('description')
    Stock = request.GET.get('stock')
    Active = request.GET.get('active')
    Display = request.GET.get('dp')
    cost = request.GET.get('costprice')
    Sell = request.GET.get('sellprice')
    Discount= request.GET.get('discount')
    proid = request.GET.get('productid')
        
    p = Product.objects.get(productid=proid)

    if Name is not None:
        p.productName = Name

    if Description is not None:
        p.productDescription = Description

    if Stock is not None:
        p.stock = int(Stock)

    if Active is not None:
        if Active == 'y':
            Active = True
        else:
            Active = False    
        p.active = Active

    if Display is not None:
        p.display = Display

    if cost is not None:
        p.costPrice = float(cost)

    if Sell is not None:
        p.sellingPrice = float(Sell)
        
    if Discount is not None:
        p.discount = float(Discount)

    p.save() 
    return JsonResponse({'result':1,'message':'Success'})

def viewProduct(request):
    proid = request.GET.get('productid')
    isALL = request.GET.get('all')
    Username = request.GET.get('username')
    

    
    list = []
    catego = []


    if isALL == 'y':
        Airport = request.GET.get('airport').upper()
        servi = request.GET.get('services').upper()     
        
        p = Product.objects.all()        
        
        cc = cat.objects.filter(airport=Airport)
        for w in cc:
            if servi == 'STORE':
                if w.store == True and w.airport == Airport:
                    ss = catSerializer(w)
                    catego.append(ss.data)

            elif servi == 'RESTAURANTS':
                if w.restaurants == True and w.airport == Airport:
                    ss = catSerializer(w)
                    catego.append(ss.data)

            else:
                if w.hotel == True and w.airport == Airport:
                    ss = catSerializer(w)
                    catego.append(ss.data)


        for a in p:
            serial = ProductSerializer(a)

            if serial.data['category']['airport'] == Airport:

                
                
                ud = userdetails.objects.get(user__username=serial.data['user']['username'])
                if ud.category == servi:
                    serialud = userdetailsSerializer(ud)
                    list.append({'product details':serial.data,'store details':serialud.data,})
                
        return JsonResponse({'result':1,'categories':catego,'Product':list})
    
    elif Username is not None:
        user1 = User.objects.get(username=Username)    
        p = Product.objects.filter(user=user1)        
        # print(p)

        for a in p:
            serial = ProductSerializer(a)
            ser = User.objects.get(username=serial.data['user']['username'])
            
            c = catSerializer(a.category)
            if c.data not in catego:
                catego.append(c.data)

            ud = userdetails.objects.get(user=ser)
            serialud = userdetailsSerializer(ud)
            list.append({'product details':serial.data,'store details':serialud.data})
        
        return JsonResponse({'result':1,'categories':catego,'Product':list})
 
    else:
        p = Product.objects.get(productid=proid)
        serial = ProductSerializer(p)
        ser = User.objects.get(username=serial.data['user']['username'])
            
        ud = userdetails.objects.get(user=ser)
        serialud = userdetailsSerializer(ud)
        list.append({'product details':serial.data,'store details':serialud.data})
         
    return JsonResponse({'result':1,'Product':list})
 

def placeOrder(request):
    proid = request.GET.get('productid')
    Username = request.GET.get('username')    
    Q = request.GET.get('quantity')

    user1 = User.objects.get(username=Username)
    p = Product.objects.get(productid=proid)
    w = wallet.objects.get(user = user1)
    w1 = wallet.objects.get(user = p.user)
    Q = int(Q)

    a = Q*(p.sellingPrice + p.sellingPrice*p.discount)
    w.amount = w.amount - a
    w1.amount = w1.amount + a 
    proid = "OD"+str(random.randint(999999,9999999))
    
    o = order(user=user1,product=p,amount=a,orderid=proid,quantity=Q)

    o.save()
    w.save()
    w1.save()
    ud = userdetails.objects.get(user = p.user)
    if ud.category == 'HOTEL':
        n = hotel(Order=o)
        n.save()
    
    
    return JsonResponse({'result':1,'message':'Success','orderid':proid})


def viewliveStoreorders(request):
    Username = request.GET.get('username')    
    
    user1 = User.objects.get(username=Username)
    
    o = order.objects.filter(product__user=user1).exclude(accept=3)
    list = []

    for a in o:
        serial = orderSerializer(a)
        ser = User.objects.get(username=serial.data['product']['user']['username'])
        ud = userdetails.objects.get(user=ser)
        serialud = userdetailsSerializer(ud)
        ho = []
        if ud.category == 'HOTEL':
            h = hotel.objects.get(Order=a)
            hotelserial = hotelSerializer(h)
            ho.append({'hotel':hotelserial.data})
        list.append({'product details':serial.data,'store details':serialud.data,'hotel':ho})
                
    return JsonResponse({'result':list})
         
        
def acceptorder(request):
    proid = request.GET.get('orderid')

    o = order.objects.get(orderid=proid)

    o.accept=0
    ud = userdetails.objects.get(user = o.product.user)
    if ud.category == 'HOTEL':
        print(1)
    else:
        n = storerestro(Order=o)
        n.save()
            
    o.save()
    

    return JsonResponse({'result':1,'status':o.accept})

def userorder(request):
    userName = request.GET.get('username')

    user1 = User.objects.get(username=userName)
    o = order.objects.filter(user=user1)

    list = []

    for a in o:
        serial = orderSerializer(a)
        list.append({'order':serial.data})
        
    return JsonResponse({'result':list})


def storeorderr(request):
    userName = request.GET.get('username')

    user1 = User.objects.get(username=userName)
    print(user1)
    o = order.objects.filter(product__user=user1)
    
    list = []

    for a in o:
        serial = orderSerializer(a)
        list.append({'order':serial.data})
        
    return JsonResponse({'result':list})
    
    
def hotelorder(request):
    odid = request.GET.get('orderid')
    checki = request.GET.get('checkin')
    checko = request.GET.get('checko')
    rating1 = request.GET.get('rating')

    d = order.objects.get(orderid=odid)
    o = hotel.objects.get(Order=d)

    if checki is not None:
        o.checkin = checki

    if checko is not None:
        o.checkout = checko

    if rating1 is not None:
        o.Rating = rating

    o.save()
    return JsonResponse({'result':1})

def storeorder(request):
    odid = request.GET.get('orderid')
    prepare = request.GET.get('preparing_packaging')
    dispatched1 = request.GET.get('dispatched')
    delivered1 = request.GET.get('delivered')
    rating1 = request.GET.get('rating')

    d = order.objects.get(orderid=odid)

    o = storerestro.objects.get(Order=d)

    if prepare is not None:
        o.preparing_packaging = True
        d.accept = 1

    if dispatched1 is not None:
        o.dispatched = True
        d.accept = 2
    
    if delivered1 is not None:
        o.delivered = True
        d.accept = 3

    if rating1 is not None:
        o.Rating = True

    d.save()
    o.save()    
    return JsonResponse({'result':1,'status':d.accept})



###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################







def showorderstate(Orderid):
    o =order.objects.get(orderid=Orderid)
    if o.accept==1 or o.accept ==10:
        #show store details
        serial = UserSerializer(o.product.user)
        ud = userdetails.objects.get(user = o.product.user)
        serialud = userdetailsSerializer(ud)

        return JsonResponse({'result':'You already have a existing delivery please complete to get more','parameter':2,'Store Details':serial.data,'more details':serialud.data,'orderid':Orderid})

    elif o.accept == 2:
        os = orderSerializer(o)
        return JsonResponse({'result':os.data,'parameter':3})



def deliverypending(request):
    Username = request.GET.get('username')

    ud = userdetails.objects.get(user__username=Username)
    if(ud.deli == False):
        ss = order.objects.filter(accept=1,delivery=None)
        
        list = []
        for s in ss:
            
            ud1 = userdetails.objects.get(user=s.product.user)
            if ud1.airport == ud.airport:
                serial = orderSerializer(s)
                ser = User.objects.get(username=serial.data['user']['username'])
                serialud = userdetailsSerializer(ud1)
                list.append({'order details':serial.data,'User details':serialud.data,'parameter':1})

        return JsonResponse({'result':list})
    else:

        return showorderstate(ud.co.orderid)



def acceptdelivery(request):
    Username = request.GET.get('username')
    Orderid=request.GET.get('orderid')            

    o = order.objects.get(orderid=Orderid)
    o.accept = 10
    user1 = User.objects.get(username=Username)

    o.delivery = user1
    o.save()

    ud = userdetails.objects.get(user__username=Username)
    ud.co = o
    ud.deli=True
    ud.save()
    return JsonResponse({'orderid':o.orderid})

def generateqr(request):
    Orderid=request.GET.get('orderid')            


    o = order.objects.get(orderid=orderid)

    return JsonResponse({'orderid':o.orderid})

def scanqr(request):
    Orderid=request.GET.get('orderid')            
    o = order.objects.get(orderid=Orderid)
    o.accept = 2
    o.save()
    return JsonResponse({'orderid':o.orderid})

def deliverproduct(request):
    Orderid=request.GET.get('orderid')            
    o = order.objects.get(orderid=Orderid)
    ud = userdetails.objects.get(user=o.delivery)
    ud.deli=False
    ud.co=None
    ud.save()
    o.accept = 3
    o.save()
    return JsonResponse({'result':'success'})


def showinfo(request):
    Orderid=request.GET.get('orderid')            
    return showorderstate(Orderid)



def deliveryhistory(request):
    Username = request.GET.get('username')
    o = order.objects.filter(delivery__username=Username)
    list = []
    for i in o:
        serial = orderSerializer(i)
        list.append(serial.data)

    return JsonResponse({'result':list})




###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################



def addAirport(request):
    Name = request.GET.get('name')
    City = request.GET.get('city')
    State = request.GET.get('state')
    Latitude = request.GET.get('latitude')
    Longitude = request.GET.get('longitude')

    s = airport(name=Name.upper(),city=City.upper(),state=State.upper(),latitude=Latitude,longitude=Longitude)
    s.save()

    return JsonResponse({'result':1})

def viewUsers(request):
    Airport = request.GET.get('airport')

    ud = userdetails.objects.filter(airport=Airport.upper()).exclude(category='NA')
    store = []
    hotel = []
    cab = []
    restro=[]

    for u in ud:
            if u.category == 'STORE':
                serial = userdetailsSerializer(u)
                store.append(serial.data)
            elif u.category == 'HOTEL':
                serial = userdetailsSerializer(u)
                hotel.append(serial.data)
            elif u.category == 'RESTAURANTS':
                serial = userdetailsSerializer(u)
                restro.append(serial.data)
            elif u.category == 'CAB':
                serial = userdetailsSerializer(u)
                cab.append(serial.data)

    return JsonResponse({'store':store,'hotel':hotel,'cab':cab,'restro':restro})



































###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################




def setdocactive(request):
    userName = request.GET.get('username')
    

    user1 = userdetails.objects.get(user__username=userName)
    
    user1.active = not user1.active
    user1.save()
    return JsonResponse({'result':1})

def risk(request):
    userName = request.GET.get('username')
    Risk = request.GET.get('risk')


    user1 = userdetails.objects.get(user__username=userName)
    
    user1.risk = int(Risk)
    user1.save()
    return JsonResponse({'result':1})

def viewdoctor(request):
    users = userdetails.objects.filter(doctor=True)
    list = []
    for u in users:
        serialud = userdetailsSerializer(u)
        list.append({'doctor':serialud.data})
        

    return JsonResponse({'result':list})

def meetcall(request):
    userName = request.GET.get('username')
    duserName = request.GET.get('docusername')
    Meet = request.GET.get('meet')
    Call = request.GET.get('chat')
    
    user1 = User.objects.get(username=userName)
    user2 = User.objects.get(username=duserName)


    if Meet is not None:
        Meet = True
    else:
        Meet = False

    if Call is not None:
        Call = True 
    else:
        Call = False       

    d = Doctor(user=user1,doctor=user2,meet=Meet,chat=Call)    
    d.save()
    return JsonResponse({'result':1})

def acceptpatient(request):
    userName = request.GET.get('username')
    duserName = request.GET.get('docusername')


    user1 = User.objects.get(username=userName)
    user2 = User.objects.get(username=duserName)    
    d = Doctor.objects.get(user=user1,doctor=user2)

    d.pending = True
    d.save()

    return JsonResponse({'result':1})

def viewpendingpatient(request):
    duserName = request.GET.get('docusername')


    user2 = User.objects.get(username=duserName)    
    
    ds = Doctor.objects.filter(doctor=user2,pending=False)

    list = []
    for d in ds:
        serial = UserSerializer(d.user)
        
        ud = userdetails.objects.get(user__username=serial.data['username'])
        serialud = userdetailsSerializer(ud)
        list.append({'Patient details':serial.data,'other info':serialud.data})
        
    return JsonResponse({'result':list})
        

class complainListView(ListAPIView):
    queryset = Complain.objects.all()
    serializer_class = complainSerializer

def complainss(request):
    userName = request.GET.get('username')
    complains = request.GET.get('complain')
    complainid1 = request.GET.get('complainid')



    user1 = User.objects.get(username=userName)

    complaint = random.randint(100,999) + random.randint(9999,10000) + user1.pk
    
    complaint = "COMP25"+str(complaint)

    print(complaint)
    comp = Complain(complain = complains,complainid = complainid1,complaintxn = complaint )
    comp.user = user1
    comp.save()    

    return JsonResponse({'result': 1})

def resolveComplain(request):
    get_id = request.GET.get('id')

    comp = Complain.objects.get(pk=get_id)
    comp.status = True

    comp.save()
    return JsonResponse({'result':1})  

def paytmCall(request):
        username1 = request.GET.get('username')
        am = request.GET.get('TXN_AMOUNT')

        user1 = User.objects.get(username = username1)
        user2 = User.objects.get(username = 'admin')
        
        # print(user2)
        complaint = random.randint(100,999) + random.randint(9999,10000) + user1.pk
    
        txn = "TXN25"+str(complaint)
        wall = wallet.objects.get(user=user2)
        # wall1 = wallet.objects.get(user=user1)
        
        transaction = Tax(amount = am, txnid = txn)
        transaction.user = user1
        # wall1.amount=0
        wall.amount = wall.amount + float(am)
        wall.save()
        # wall1.save()
        transaction.save()
        return JsonResponse({'result':1})



class transactionListView(ListAPIView):
    queryset = Tax.objects.all()
    serializer_class = transactionSerializer
        