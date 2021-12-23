from rest_framework import serializers

from Main_Menu.models import mainmenu, category


class mainmenuserilalizers(serializers.ModelSerializer):
    class Meta():
        model=mainmenu
        fields= '__all__'

class categoryserilizers(serializers.ModelSerializer):
    class Meta():
        model=category
        fields='__all__'

