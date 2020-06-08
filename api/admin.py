from django.contrib import admin
from api.models import userdetails,Product,wallet,order,hotel,storerestro,Complain,Tax

# Register your models here.

admin.site.register(userdetails)
admin.site.register(Product)
admin.site.register(wallet)
admin.site.register(order)
admin.site.register(hotel)
admin.site.register(Tax)
admin.site.register(Complain)
admin.site.register(storerestro)
