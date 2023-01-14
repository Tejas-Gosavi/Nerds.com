from rest_framework import routers, serializers, viewsets
from .models import User

class UserSerializer(serializers.ModelSerializer):
    personalData = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'personalData', 'address']
    
    def get_personalData(self, obj):
        return obj.getPersonalData()

    def get_address(self, obj):
        return obj.getAddress()