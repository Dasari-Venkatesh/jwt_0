from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer,MyObtainTokenSerializer
from .permissions import IsAdminUser,IsClientUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

class ClientViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated,IsClientUser,]
    authentication_classes = [JWTAuthentication,]

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(user_type='Client')




class AdminViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,IsAdminUser,)
    authentication_classes = [JWTAuthentication,]

    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(user_type='Admin')


class MyObtainTokenView(TokenObtainPairView):
    serializer_class = MyObtainTokenSerializer