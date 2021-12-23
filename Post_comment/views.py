from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin

from . import serializers
from .models import *
from .serializers import BlogPost_Serializer


class RetriveData(GenericAPIView,RetrieveModelMixin):
    serializer_class = BlogPost_Serializer
    queryset = BlogPost.objects.all()
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Retrivelist(GenericAPIView,ListModelMixin):
    serializer_class = BlogPost_Serializer
    queryset = BlogPost.objects.all()
    def get(self,request,**kwargs):
        return self.list(request,**kwargs)


class CommentModel(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = serializers.Comment_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ReplyModel(viewsets.ModelViewSet):
    queryset = ReplyModel.objects.all()
    serializer_class = serializers.Reply_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
