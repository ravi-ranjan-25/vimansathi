from django.shortcuts import render
import boto3
# Create your views here.
import xlwt
from xlwt import Workbook 
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse
from api.models import userdetails,Product,wallet,order,hotel,storerestro,Doctor,Complain,Tax,cat,airport,airline,routes,days,book,productComplain
from django.contrib.auth.models import User
import json
from recommendation.models import userinteraction
from api.models import userdetails,Product,wallet,order,hotel,storerestro,Doctor,Complain,Tax,cat,airport,airline,routes,days,book
from django.contrib.auth.models import User
# from api.serializers import orderSerializer,userdetailsSerializer,bookSerializer,ProductSerializer
from api.serializers import ProductSerializer,orderSerializer,userdetailsSerializer,UserSerializer,complainSerializer,transactionSerializer,catSerializer,hotelSerializer,hotelSerializer,airlineSerializer,routesSerializer,daysSerializer,airportSerializer,transactionSerializer,bookSerializer,messageSerializer
import datetime

def recommendationget(request):
    Username = request.GET.get('username')
    Airport = request.GET.get('airport')

    personalizeRt = boto3.client('personalize-runtime',region_name='ap-south-1')

    response = personalizeRt.get_recommendations(
        campaignArn = 'arn:aws:personalize:ap-south-1:413538326238:campaign/viman-campaign',
        userId = Username)

    listshop = []
    listrestro = []
    listhotel = []
    for i in response['itemList']:
        print(i['itemId'])
        pro = Product.objects.get(productid=i['itemId'])
        ud = userdetails.objects.get(user=pro.user)
        if ud.airport == Airport.upper():
            serial = ProductSerializer(pro)
            if ud.category == 'STORE':
                listshop.append(serial.data)
            elif ud.category == 'RESTAURANTS':
                listrestro.append(serial.data)
            elif ud.category == 'HOTEL':
                listhotel.append(serial.data)        

    return JsonResponse({'store':listshop,'restro':listrestro,'hotel':listhotel})

def createpackage(request):
    Username = request.GET.get('username')
    Origin = request.GET.get('origin')
    Airport = request.GET.get('destination')
    # Date = request.GET.get('date')

    D = request.GET.get('Date')
    D=datetime.datetime.strptime(D, '%Y-%m-%d')

    r  = routes.objects.filter(origin=Origin.upper(),destination=Airport.upper())
    flight = []
    for i in r:
        print(i)
        Da = days.objects.filter(date=D,Route=i)[-1]
    
        serial = daysSerializer(da)
        flight.append(serial.data)

    
    personalizeRt = boto3.client('personalize-runtime',region_name='ap-south-1')

    response = personalizeRt.get_recommendations(
        campaignArn = 'arn:aws:personalize:ap-south-1:413538326238:campaign/viman-campaign',
        userId = Username)

    listshop = []
    listrestro = []
    listhotel = []
    for i in response['itemList']:
        print(i['itemId'])
        pro = Product.objects.get(productid=i['itemId'])
        ud = userdetails.objects.get(user=pro.user)
        if ud.airport == Airport.upper():
            # serial = ProductSerializer(pro)
            serial = ProductSerializer(pro)
            if ud.category == 'STORE':
                listshop.append(serial.data)
            elif ud.category == 'RESTAURANTS':
                listrestro.append(serial.data)
            elif ud.category == 'HOTEL':
                listhotel.append(serial.data)        
    

    if len(listshop) > 0:
        shop = listshop[0]
    else:
        ud = userdetails.objects.filter(category='SHOP',airport=Airport)[0]
        pro = Product.objects.filter(user__username=ud.user.username)[0]
        serial = ProductSerializer(pro)
        shop = serial.data

    if len(listrestro) > 0:
        restro = listrestro[0]
    else:
        ud = userdetails.objects.filter(category='RESTAURANTS',airport=Airport)[0]
        pro = Product.objects.filter(user__username=ud.user.username)[0]
        serial = ProductSerializer(pro)
        restro = serial.data

   
    if len(listhotel) > 0:
        shop = listhotel[0]
    else:
        ud = userdetails.objects.filter(category='HOTEL',airport=Airport)[0]
        pro = Product.objects.filter(user__username=ud.user.username)[0]
        serial = ProductSerializer(pro)
        hotel = serial.data
   
    


    return JsonResponse({'store':store,'restro':restro,'hotel':hotel,'flight':flight})



def createDataset(reqeust):
    # wb = Workbook()
    # sheet1 = wb.add_sheet('Sheet 1')


    userall = User.objects.all()
    c = 1
    list = []
    for u in userall:
        try: 
            ud = userdetails.objects.get(user__username=u.username)
            if ud.category == 'NA':
                Username = u.username
                Loyality = ud.points

                list.append({'USER_ID':Username,'vip':Loyality})
        except:
            continue
            
    
    # wb.save('users.csv')

    return JsonResponse({'result':list})

def createproductDataset(reqeust):
    # wb = Workbook()
    # sheet1 = wb.add_sheet('Sheet 1')


    pro = Product.objects.all()
    c = 1
    list = []
    for p in pro:
        proid = p.productid
        category = p.category.name
        rating = p.rating
        airport = p.category.airport
        price = p.sellingPrice
        list.append({'ITEM_ID':proid,'category':p.category.name,'rating':rating,'airport':airport,'price':price})
    
    # wb.save('users.csv')

    return JsonResponse({'result':list})

def userproductinteractions(request):
    ord = order.objects.all()
    c = 1
    list = []
    for o in ord:
        proid = o.product.productid
        Username = o.user.username
        
        list.append({'USER_ID':Username,'ITEM_ID':proid,'TIMESTAMP':int(o.time.timestamp()*1000),'EVENT_TYPE':'PURCHASE'})


    return JsonResponse({'result':list})

# def createuserSchema(request):
#     personalize = boto3.client('personalize')
    

#     schema_name = 'orderinteractions'
    
#     # Define the schema for your dataset
#     schema = {
#         "type": "record",
#         "name": "Users",
#         "namespace": "com.amazonaws.personalize.schema",
#         "fields": [
#             {
#                 "name": "USER_ID",
#                 "type": "string"
#             },
#             {
#                 "name": "LOYALITY",
#                 "type": "string",
#                 "categorica"
#             }
#         ],
#         "version": "1.0"
#     }
#     print(1)
    
#     # Create the schema for Amazon Personalize
#     create_schema_response = personalize.create_schema(
#         name = schema_name,
#         schema = json.dumps(schema)
#     )
    
#     #To get the schema ARN, use the following lines
#     schema_arn = create_schema_response['schemaArn']
#     print('Schema ARN:' + schema_arn )

#     return JsonResponse({'result':1})
    

# def createSchema(request):
#     personalize = boto3.client('personalize')
    

#     schema_name = 'orderinteractions'
    
#     # Define the schema for your dataset
#     schema = {
#         "type": "record",
#         "name": "Interactions",
#         "namespace": "com.amazonaws.personalize.schema",
#         "fields": [
#             {
#                 "name": "USER_ID",
#                 "type": "string"
#             },
#             {
#                 "name": "ITEM_ID",
#                 "type": "string"
#             },
#             {
#                 "name": "EVENT_TYPE",
#                 "type": "string"
#             },
#             { 
#                 "name": "TIMESTAMP",
#                 "type": "long"
#             }
#         ],
#         "version": "1.0"
#     }
    
    
#     # Create the schema for Amazon Personalize
#     create_schema_response = personalize.create_schema(
#         name = schema_name,
#         schema = json.dumps(schema)
#     )
    
#     #To get the schema ARN, use the following lines
#     schema_arn = create_schema_response['schemaArn']
#     print('Schema ARN:' + schema_arn )    
#     # ARN:arn:aws:personalize:ap-south-1:413538326238:schema/orderinteractions
#     return JsonResponse({'result':1})


def clickEvent(request):
    proid = request.GET.get('productid')
    Username = request.GET.get('username')
    Value = request.GET.get('amount')
    Event = request.GET.get('event_type')
    
    r = userinteraction(USER_ID=Username,ITEM_ID=proid,EVENT_TYPE=Event.upper(),EVENT_VALUE=float(Value))
    r.save()

    return JsonResponse({'result':1})

def interationsUser(request):

    userall=userinteraction.objects.all()
    list1 = []
    list = []
    count = 0
    for u in userall:
        list.append({'USER_ID':u.USER_ID,'ITEM_ID':u.ITEM_ID,'EVENT_TYPE':u.EVENT_TYPE,'EVENT_VALUE':u.EVENT_VALUE,'TIMESTAMP':int(u.TIMESTAMP.timestamp())})
        if u.EVENT_TYPE == 'CLICK':
            U = {'USER_ID':u.USER_ID,'ITEM_ID':u.ITEM_ID,'EVENT_TYPE':u.EVENT_TYPE,'EVENT_VALUE':u.EVENT_VALUE,'TIMESTAMP':int(u.TIMESTAMP.timestamp())}
            if U not in list1 and u.EVENT_TYPE== 'CLICK':   
                count += 1
                list1.append(U)
    return JsonResponse({'count':count,'result':list})    
   