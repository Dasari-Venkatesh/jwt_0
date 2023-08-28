from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer

class ClientAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        clients = CustomUser.objects.filter(user_type='Client')
        serializer = UserSerializer(clients, many=True)
        return Response(serializer.data)

class AdminAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        admins = CustomUser.objects.filter(user_type='Admin')
        serializer = UserSerializer(admins, many=True)
        return Response(serializer.data)
