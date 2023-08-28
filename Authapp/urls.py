from django.urls import path
from .views import ClientAPIView, AdminAPIView

urlpatterns = [
    path('clients/', ClientAPIView.as_view(), name='client-list'),
    path('admins/', AdminAPIView.as_view(), name='admin-list'),
]
