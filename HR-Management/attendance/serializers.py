from rest_framework import serializers
from coreApp.models import Attendance 
from user.serializers import Userserializer  

class Attendanceserializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    user = Userserializer(read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id']

