from rest_framework import serializers
from .models import *


class BlogPost_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'


class Reply_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyModel
        fields = '__all__'

