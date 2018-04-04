from django.contrib.auth.models import User, Group
from .models import Restaurant, HappyHour
from rest_framework import serializers


class RestaurantSerializer(serializers.Serializer):
    class Meta:
        model = Restaurant
        fields = ('id','pub_date', 'name', 'lat', 'long', 'type')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

