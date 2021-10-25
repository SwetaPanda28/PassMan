from rest_framework import viewsets
from .serializers import PasswordSerializer, UserSerializer,PasswordManagerSerializer
from . import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)


class PasswordManagerViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class=PasswordManagerSerializer

    def get_queryset(self):
        user=self.request.user
        return models.PasswordManager.objects.filter(user_id=user)


class PasswordViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    serializer_class=PasswordSerializer

    def get_queryset(self):
        man=models.PasswordManager.objects.get(user=self.request.user)
        return man.password_set.all()
