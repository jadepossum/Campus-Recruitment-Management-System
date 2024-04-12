from rest_framework import status
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Jobs,Student,Internship,Certification
from .serializers import JobSerializer,UserSerializer,StudentSerializer,InternshipSerializer,CertificationSerializer 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@api_view(["POST"])
@csrf_exempt
def userLogin(request):
    username = request.data['username']
    user = get_object_or_404(User, username=username)
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not found"},status=status.HTTP_404_NOT_FOUND)
    token ,created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    studentDetails = Student.objects.filter(roll_number = username).first()
    internshipDetails = Internship.objects.filter(roll_number = username)
    certificationDetails = Certification.objects.filter(roll_number = username)
    return Response({"studentDetails":StudentSerializer(studentDetails,many=False).data if studentDetails else {"data":"data unavailable"},
                     "internDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else {"data":"data unavailable"},
                     "certificationDetails":CertificationSerializer(certificationDetails,many=True).data if certificationDetails.exists() else {"data":"data unavailable"},
                     "token":token.key,"user":serializer.data
                     })

@api_view(["POST"])
def userSingup(request):
    serializer  = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user= user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def userAuthenticate(request):
    token = request.data['token']
    try:
        username = Token.objects.get(key=token).user
        user = User.objects.get(username=username)
        serializer = UserSerializer(instance = user)
        # studentDetails = Student.objects.filter(roll_number = username).first()
        # internshipDetails = Internship.objects.filter(roll_number = username)
        # certificationDetails = Certification.objects.filter(roll_number = username)
        return Response({"user":serializer.data,"token":token})
        # return Response({"studentDetails":StudentSerializer(studentDetails,many=False).data if studentDetails else {"data":"data unavailable"},
        #                 "internDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else {"data":"data unavailable"},
        #                 "certificationDetails":CertificationSerializer(certificationDetails,many=True).data if certificationDetails.exists() else {"data":"data unavailable"},
        #                 "token":token,"user":serializer.data
        #              })
    except:
        return Response({"details ":"not found"},status=status.HTTP_404_NOT_FOUND)


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


@api_view(["POST"])
def sendProfile(request):
    username = request.data['username']
    studentDetails = Student.objects.filter(roll_number = username).first()
    internshipDetails = Internship.objects.filter(roll_number = username)
    certificationDetails = Certification.objects.filter(roll_number = username)
    return Response({"studentDetails":StudentSerializer(studentDetails,many=False).data if studentDetails else {"data":"data not found"},
                     "internDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else {"data":"data not found"},
                     "certificationDetails":CertificationSerializer(certificationDetails,many=True).data if certificationDetails.exists() else {"data":"data not found"},
                     })

@api_view(["POST"])
def uploadCert(request):
    serializer = CertificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    else:
        return Response(serializer.errors,status=400)