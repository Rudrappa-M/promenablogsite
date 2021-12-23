from rest_framework import serializers

from Newsletter.models import Subscription, Newsletter

class Subscriptionserilaizers(serializers.ModelSerializer):
    class Meta():
        model=Subscription
        fields='__all__'


class Newsletterserilaizers(serializers.ModelSerializer):
    class Meta():
        model = Newsletter
        fields= '__all__'