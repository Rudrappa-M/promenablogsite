# from django.http import HttpResponse
# from django.shortcuts import render
from coreapi.auth import TokenAuthentication
from rest_framework import viewsets, generics, mixins
# # Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from Main_Menu.models import mainmenu, category
from Main_Menu import serializers

from Main_Menu.serializers import mainmenuserilalizers, categoryserilizers


class RetriveData(GenericAPIView,RetrieveModelMixin):
    serializer_class = mainmenuserilalizers
    queryset = mainmenu.objects.all()
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Retrivelist(GenericAPIView,ListModelMixin):
    serializer_class = mainmenuserilalizers
    queryset = mainmenu.objects.all()
    def get(self,request,**kwargs):
        return self.list(request,**kwargs)

class CreateRetrieve(GenericAPIView,RetrieveModelMixin):
    serializer_class = categoryserilizers
    queryset = category.objects.all()
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)

class CreateRetrivelist(GenericAPIView,ListModelMixin):
    serializer_class = categoryserilizers
    queryset = category.objects.all()
    def get(self,request,**kwargs):
        return self.list(request,**kwargs)







