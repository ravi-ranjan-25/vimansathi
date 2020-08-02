"""vimansathi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework import routers
from .views import complainListView,transactionListView
from cab.views import measureLoyality
# from .views import EventListView


urlpatterns = [
# path('/user', , name = "userConsumptionN"),
    path('signup',views.signup , name = "signup"),
    path('login',views.login , name = "login"),
    path('addproduct',views.addProduct,name="add"),
    path('editproduct',views.editproduct,name="add"),
    path('viewproduct',views.viewProduct,name="add"),
    path('placeorder',views.placeOrder,name="add"),
    path('viewpendingorders',views.viewliveStoreorders,name="add"),
    path('acceptorder',views.acceptorder,name="add"),
    path('showuserorder',views.userorder,name="add"),
    path('showstoreorder',views.storeorderr,name="add"),
    path('hotelcheck',views.hotelorder,name="add"),
    path('addhotel',views.staticimg,name="add"),
    path('updatecheckincheckout',views.addcheckin,name="add"),

# path('storeordeer',views.userorder,name="add"),
    path('processorder',views.storeorder,name="add"),
    
    #############################################################3
    path('doctor/active',views.setdocactive,name="add"),
    path('risk',views.risk,name="add"),
    path('doctor/viewdoctor',views.viewdoctor,name="add"),
    path('doctor/meet',views.meetcall,name="add"),
    path('doctor/chat',views.meetcall,name="add"),
    path('doctor/accept',views.acceptpatient,name="add"),
    path('doctor/viewpendingpatient',views.viewpendingpatient,name="add"),

####################################################################################

    path('resolvecomplains',views.resolveComplain,name = "resolve"),
    path('complain',views.complainss , name = "comp"),
    # path('viewconsumption',views.viewConsumption , name = "comp2"),
    path('showcomplains',complainListView.as_view(),name = "complain"),
    # path('donate',views.paytmCall,name = "paytmcall"),
    path('software/paytmcall',views.paytmCall1,name = "paytmcall"),
    path('transaction',transactionListView.as_view(),name = "transaction"),
    path('showtransaction',views.showtrans,name = "transaction"),
    path('predictfare',views.cxcontact,name = "transaction"),


#################################################################################

    path('delivery/live',views.deliverypending,name = "resolve"),
    path('delivery/accept',views.acceptdelivery,name = "resolve"),
    path('delivery/generateqr',views.generateqr,name = "resolve"),
    path('delivery/scanqr',views.scanqr,name = "resolve"),
    path('delivery/deliverproduct',views.deliverproduct,name = "resolve"),
    path('delivery/info',views.showinfo,name = "resolve"),
    path('delivery/history',views.deliveryhistory,name = "resolve"),
    
    ##############################################################################
    
    
    path('getwallet',views.getWallet,name = "resolve"),
    path('admin/addairport',views.addAirport,name = "resolve"),
    path('admin/viewUsers',views.viewUsers,name = "resolve"),
    path('admin/resolvecomplains',views.resolveComplain,name = "resolve"),
    path('admin/complain',views.complainss , name = "comp"),
    path('admin/showcomplains',complainListView.as_view(),name = "complain"),
   
    ##############################################################################

    path('admin/addairline',views.addAirline,name = "resolve"),
    path('admin/addflight',views.addFlight,name = "resolve"),
    path('admin/setfrequency',views.setFrequency,name = "resolve"),
    path('admin/listAirline',views.listAirline,name = "resolve"),
    path('admin/listairport',views.listAirport,name = "resolve"),
    path('admin/listflight',views.listflight,name = "resolve"),
    path('admin/godseye',views.godseye,name = "resolve"),
    path('admin/approveshop',views.approveShop,name = "resolve"),
    path('admin/disableShop',views.complainShop,name = "resolve"),
    path('admin/approvallist',views.approves,name = "resolve"),
    path('admin/recentflightOrders',views.recentflightOrders,name = "resolve"),
    path('admin/notifyStore',views.notifyStore,name = "resolve"),
    path('admin/nlpreviews',views.nlpreviews,name = "resolve"),
    path('getmessages',views.getmessages,name = "resolve"),
    path('findFlights',views.findFlights,name = "resolve"),
    path('bookFlights',views.bookFlights,name = "resolve"),

    #####################################################################
    path('addstorerating',views.updatestoreRating,name = "resolve"),
    path('addhotelrating',views.hotelRating,name = "resolve"),
    path('viewcurrentorders',views.currentorders,name = "resolve"),
    path('cancelorder',views.cancelOrder,name = "resolve"),
    path('cancelcab',views.cancelcab,name = "resolve"),
    path('addcomplains',views.addComplains,name = "resolve"),
    path('riskinarea',views.arogyasetu,name = "resolve"),
    path('addreview',views.addReview,name = "resolve"),
    path('showProductReview',views.showProductReview,name = "resolve"),
    path('downloadwords',views.downloadwords,name = "resolve"),
    
    path('measureloyality',measureLoyality,name = "resolve"),


]
