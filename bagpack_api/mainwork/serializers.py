from rest_framework.serializers import ModelSerializer, IntegerField, Serializer
from django.contrib.auth.models import User

from .models import ItemBook

class ItemBookSerializer(ModelSerializer):
    # userid = IntegerField()
    
    class Meta:
        model = ItemBook
        fields = '__all__'
        
# class ItemBookSerializerList(Serializer):
#     userid = IntegerField()


class UserSignUp(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        
class UserSignIn(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        