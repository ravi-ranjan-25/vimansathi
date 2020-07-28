from celery import shared_task,app
from time import sleep
from cab.models import cabOrder
from vimansathi.celery import app
from .funcs import dispatch,isInside,dispatchdilevery

@app.task
def bookcab1(cid):
    c = cabOrder.objects.get(cabid=cid)
    c.accept = -1
    c.save()
    d = dispatch(cid)
    return d

@app.task
def dispatchDelivery(od):
    o = order.objects.get(orderid=od)
    o.accept = 1
    o.save()
    d = dispatchdilevery(od)
    return d
