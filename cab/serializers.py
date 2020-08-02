from rest_framework import serializers
from django.contrib.auth.models import User
# from api.models import Product,order,userdetails,Complain,Tax,cat
from cab.models import carClass,cabdetails,cabOrder
# from api.serializers import UserSerializers

# class kafkaSerializer:
class kafkaSerializer(serializers.Serializer):
    username = serializers.CharField() 

class carClassSerializer(serializers.Serializer):
    cartype = serializers.CharField()
    seat = serializers.IntegerField()

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()


class cabdetailsSerializer(serializers.Serializer):
    user = UserSerializer()
    cartype = carClassSerializer()
    carModel = serializers.CharField()
    carRegistration = serializers.CharField()
    carColor = serializers.CharField()
    rating = serializers.FloatField()
    totalRides = serializers.IntegerField()


class cabOrderSerializer(serializers.Serializer):
    user = UserSerializer()
    cab = cabdetailsSerializer()
    origin = serializers.CharField()
    # Cabtype = serializers.CharField()
    cabid = serializers.CharField()
    destination = serializers.CharField()
    latitudeOrigin = serializers.CharField()
    longitudeOrigin = serializers.CharField()
    latitudeDestination = serializers.CharField()
    longitudeDestination = serializers.CharField()
    seat = serializers.IntegerField()
    price=serializers.FloatField()
    accept = serializers.IntegerField()
    pickupTime = serializers.DateTimeField()
    time = serializers.DateTimeField()
