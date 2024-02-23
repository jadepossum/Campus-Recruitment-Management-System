from rest_framework import serializers
from .models import Jobs,Users

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'