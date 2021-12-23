import datetime

from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import Userserializer, LoginSerializer #ChangePasswordSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from.models import User
import jwt,datetime
from rest_framework import generics, status


class RegisterView(generics.GenericAPIView):
    serializer_class = Userserializer
    def post(self,request):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("user is not found")
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")
        payload={
            "id":user.id,
            "exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            "iat":datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')
        return Response({
            "jwt":token
        })



#CHANGE PASSWORD
# from rest_framework import status
# from rest_framework import generics
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from .serializers import ChangePasswordSerializer
# from rest_framework.permissions import IsAuthenticated
#
# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """
#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj
#
#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)
#
#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }
#
#             return Response(response)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

