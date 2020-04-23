# users/views.py
from rest_framework import generics
from django.contrib.auth import authenticate ,get_user_model
from iotdeviseRegistration.models import Registerdevice
from rest_framework.response import Response
from .serializers import RegisterdeviceSerializer
from django.conf import settings
from rest_framework import permissions

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset =  Registerdevice.objects.all()
    serializer_class = RegisterdeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

