from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Jobs,Users
from .serializers import JobSerializer
# Create your views here.

@api_view(["GET"])
def getJobPost(request):
    JobPosts = Jobs.objects.all()
    serealizer = JobSerializer(JobPosts,many=True)
    return Response(serealizer.data)

@api_view(["POST"])
def setJobPost(request):
    serealizer = JobSerializer(data=request.data)
    if serealizer.is_valid():
        serealizer.save()
    return Response(serealizer.data)