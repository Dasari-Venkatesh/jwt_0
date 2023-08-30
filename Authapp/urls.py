from rest_framework.routers import DefaultRouter
from .views import ClientViewSet,AdminViewSet,MyObtainTokenView
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'admins', AdminViewSet, basename='admin')

urlpatterns =[
     path("",include(router.urls)),
     path("token/",MyObtainTokenView.as_view(),name="token"),
      path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
     ]
