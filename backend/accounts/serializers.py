from rest_framework import serializers

from charities.models import Benefactor, Charity
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'address' ,
                  'gender' , 'age' , 'description' , 'first_name' ,
                  'last_name' , 'email']

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user






