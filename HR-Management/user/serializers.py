from rest_framework import serializers
from coreApp.models import User   

class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id']

