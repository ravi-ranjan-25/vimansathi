from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Product,order,userdetails,Complain,Tax,cat

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()

class catSerializer(serializers.Serializer):
    name = serializers.CharField()
    airport = serializers.CharField()

class userdetailsSerializer(serializers.Serializer):
    user = UserSerializer()
    mobile = serializers.CharField()
    admin = serializers.BooleanField()
    objectname = serializers.CharField()
    airport = serializers.CharField()
    category = serializers.CharField()
    serves = catSerializer()
    active = serializers.BooleanField()
    doctor = serializers.BooleanField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    active = serializers.BooleanField()
    risk = serializers.IntegerField()


class ProductSerializer(serializers.Serializer):
    user = UserSerializer()
    productName = serializers.CharField()
    productid = serializers.CharField()
    productDescription = serializers.CharField()
    stock = serializers.IntegerField()
    active = serializers.BooleanField()
    display = serializers.CharField()
    costPrice = serializers.FloatField()
    sellingPrice = serializers.FloatField()
    discount = serializers.FloatField()
    category = catSerializer()

class orderSerializer(serializers.Serializer):
    user = UserSerializer()
    product = ProductSerializer()
    amount = serializers.FloatField()
    orderid = serializers.CharField()
    accept = serializers.IntegerField()
    quantity = serializers.IntegerField()


# class EventSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = event
#         fields = '__all__'

class complainSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('Complain')
    
    class Meta:
        model = Complain
        fields = '__all__'

    def Complain(self,wall): 
         user1 = wall.user.username
        #  print(username)
         return user1


class transactionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('Complain')
    
    class Meta:
        model = Tax
        fields = '__all__'

    def Complain(self,wall): 
         user1 = wall.user.username
        #  print(username)
         return user1
    