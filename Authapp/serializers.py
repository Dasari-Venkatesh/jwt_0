from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type','password']

    def create(self, validated_data):
        user=CustomUser.objects.create(username=validated_data['username'],email=validated_data['email'],user_type=validated_data['user_type'])
        user.set_password(validated_data['password'])
        user.save()
        
        return validated_data 

class MyObtainTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)

        #custom claims
        token['username'] = user.username
        token['user_type'] = user.user_type
        
        return token