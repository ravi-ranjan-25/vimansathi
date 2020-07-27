from celery import shared_task,app
from time import sleep
from cab.models import cabOrder
from vimansathi.celery import app
from .funcs import dispatch,isInside

@app.task
def bookcab1(cid):
    c = cabOrder.objects.get(cabid=cid)
    c.accept = -1
    c.save()
    d = dispatch(cid)
    return d