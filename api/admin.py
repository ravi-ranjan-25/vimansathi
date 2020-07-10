from django.contrib import admin
from api.models import userdetails,Product,wallet,order,hotel,storerestro,Complain,Tax,cat,airline,routes,days,airport

# Register your models here.

admin.site.register(userdetails)
admin.site.register(Product)
admin.site.register(wallet)
admin.site.register(order)
admin.site.register(hotel)
admin.site.register(Tax)
admin.site.register(Complain)
admin.site.register(storerestro)
admin.site.register(cat)
admin.site.register(airline)
admin.site.register(routes)
admin.site.register(days)
admin.site.register(airport)