from rest_framework import serializers
from .models import Student,Internship,Certification,Jobs,ImportantDates,EligibilityCriteria
from django.contrib.auth.models import User

# class JobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Jobs
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id','username','password','email']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['roll_number','name','email','cgpa','skills','twelthPercentage','tenthCGPA','BackLogCount','github_profile','linkedin_profile','portfolio_website','phone']

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class ImportantDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantDates
        fields = ['id','Job','Date','EventTitle']
        # fields = '__all__'

class EligibilityCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EligibilityCriteria
        fields = '__all__'