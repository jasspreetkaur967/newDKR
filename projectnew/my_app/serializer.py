#from dataclasses import fields
#from pyexpat import model
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
      #  fields = ("stu_id","stu_name")