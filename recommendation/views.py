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
                
                list.append({'USER_ID':Username})
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
        
        list.append({'USER_ID':Username,'ITEM_ID':proid,'TIMESTAMP':o.time,'EVENT_TYPE':'PURCHASE'})


    return JsonResponse({'result':list})
