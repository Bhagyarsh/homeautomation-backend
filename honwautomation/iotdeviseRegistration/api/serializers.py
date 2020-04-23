# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from iotdeviseRegistration.models import Registerdevice
import datetime
from django.utils import timezone

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class RegisterdeviceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Registerdevice
        fields = ('user','deviceID', 'registerdatatime','logo')
