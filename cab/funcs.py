from api.models import userdetails,Product,wallet,order,hotel,storerestro,Doctor,Complain,Tax,cat,airport,airline,routes,days,book
from cab.models import carClass,cabdetails,cabOrder
from django.contrib.auth.models import User
import s2geometry as s2
import requests
from time import sleep

def isInside(lat,long,p):
    latlng1 = s2.S2LatLng.FromDegrees(lat,long)
    cell1 = s2.S2CellId(latlng1)
    return p.contains(cell1)



def dispatch(cid):
    wasassigned = []
    C = cabOrder.objects.get(cabid=cid)
    
    latlng = s2.S2LatLng.FromDegrees(float(C.latitudeOrigin),float(C.longitudeOrigin))
    cell = s2.S2CellId(latlng)
    
    
    link1 = 'https://vimansathi.firebaseio.com/cab.json'
    response = requests.get(link1)
    response = response.json()
    userall = userdetails.objects.all()
    

    
    count = 13
    while True:
        try:
            if isInside(float(response[u.user.username]['latitude']),float(response[u.user.username]['longitude']),p) == True:
                print(1)
        except:
            continue        
        p = cell.parent(count)
        for u in userall:
            if u.user.username not in wasassigned:
                
                print(u.user.username)
                if isInside(float(response[u.user.username]['latitude']),float(response[u.user.username]['longitude']),p) == True:
                    
                    # if isInside(float(response['sunil']['latitude']),float(response['sunil']['longitude']),p) == True:
                        print('inside this loop')
                        if u.user.username != 'sunil' and u.category == 'CAB' and u.cabIdle == True:
                            c = cabdetails.objects.get(user__username = u.user.username)
                            ud = userdetails.objects.get(user__username = u.user.username)
                            if c.cartype == C.cartype:
                                print(1)
                                print(ud.user.username)
                                C.cab = c
                                ud.cabIdle = False
                                C.accept = 11
                                c.save()
                                C.save()
                                sleep(30)
                                if C.accept == 11:
                                    C.cab = None                       
                                    ud.cabIdle = True
                                    C.accept = -10
                                    C.save()
                                    c.rejected += 1
                                    wasassigned.append(u.user.username)
                                else:
                                    ud.cabO = C
                                    c.accepted += 1
                                    break  
                
        print(1)
        count -= 1
        if C.accept == 1: 
            return True
            break
        elif count == 10:
            return False
            break

    return True        

def dispatchdilevery(od):
    wasassigned = []
    C = order.objects.get(orderid=od)
    ud1 = userdetails.objects.get(user__username=C.product.user.username)

    latlng = s2.S2LatLng.FromDegrees(float(ud1.latitude),float(ud1.longitude))
    cell = s2.S2CellId(latlng)
    
    
    link1 = 'https://vimansathi.firebaseio.com/delivery.json'
    response = requests.get(link1)
    response = response.json()
    userall = userdetails.objects.all()
    


    count = 13
    while True:
        p = cell.parent(count)
        for u in userall:
            if u.user.username not in wasassigned:
                try:
                    if u.category == 'DELIVERY' and u.deli == False:
                        if isInside(float(response[u.user.username]['latitude']),float(response[u.user.username]['longitude']),p) == True:
                            ud = userdetails.objects.get(user__username = u.user.username)
                            C.delivery = ud.user
                            ud.deli = False
                            C.accept = 11
                            C.save()
                            sleep(15)
                            if C.accept == 11:
                                C.delivery = None                       
                                ud.deli = False
                                C.accept = 100
                                C.save()
                                ud.rejected += 1
                                wasassigned.append(u.user.username)
                            else:
                                ud.co = C
                                ud.accepted += 1
                                break  
                except:
                    continue
        print(1)
        count -= 1
        if C.accept == 1: 
            return True
            break
        elif count == 10:
            return False
            break

    return True        
