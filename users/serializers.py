from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from.models import User

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=555, min_length=3)
    password =serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['email','password']


#CHANGE_PASSWORD

# from rest_framework import serializers
# from django.contrib.auth.models import User
#
# class ChangePasswordSerializer(serializers.Serializer):
#
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#     class Meta:
#         model = User
#         fields=['old_password','new_password']











