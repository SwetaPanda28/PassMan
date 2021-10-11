import base64
from django.http.response import HttpResponse, HttpResponseBadRequest,JsonResponse
from django.shortcuts import render
from django.http import HttpRequest, request
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PasswordSerializer, UserSerializer,PasswordManagerSerializer
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes,authentication_classes
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

    def get_queryset(self,key):
        user=self.request.user
        man=models.PasswordManager.objects.get(user=user)
        dets=[]
        for det in man.password_set.all():
            det.password =det.readPass(key)
            dets.append(det)
        return dets

    def retrieve(self,request,pk):
        pk=base64.urlsafe_b64decode(pk).decode()
        return JsonResponse(self.serializer_class(self.get_queryset(pk),many=True).data,safe=False)
    
    def list(self,request):
        return HttpResponseBadRequest('Pass the key as http(s)://<url>/password/<key>/')

        