from rest_framework import  fields, serializers

from mainApp import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['url', 'username', 'email', 'is_staff']
        read_only_fields = ['url', 'username', 'email', 'is_staff']



class PasswordManagerSerializer(serializers.ModelSerializer):
    password_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='password-detail'
        
    )
    class Meta:
        model=models.PasswordManager
        fields="__all__"

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Password
        fields = '__all__'
