from rest_framework import serializers
from .models import User, InventoryItem, Request, Transaction
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'club']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    
    def validate(self,data):
        username=data.get("username")
        password=data.get("password")
        user=authenticate(username=username,password=password)
        
        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        
        if not user.is_active:
            raise AuthenticationFailed("user is disabled")
        
        return{"user":user}