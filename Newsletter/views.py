from django.shortcuts import render
from rest_framework import viewsets
# # Create your views here.
from Newsletter.models import  Newsletter, Subscription
from Newsletter import serializers
# Create your views here.
class post_newsletter(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = serializers.Newsletterserilaizers


class post_Subscribe(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = serializers.Subscriptionserilaizers