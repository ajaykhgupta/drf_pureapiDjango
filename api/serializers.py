import imp
import rlcompleter
from unicodedata import name
from rest_framework import serializers
from .models import Student
# from .models import Student

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    #  create new record
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    # update existing record
    # instance -> existing data stored in database
    # validated_data -> new data from user for updation
    def update(self,instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance