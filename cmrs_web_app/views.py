from rest_framework import status
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student,Internship,Certification,Jobs,ImportantDates,EligibilityCriteria
from .serializers import UserSerializer,StudentSerializer,InternshipSerializer,CertificationSerializer,JobSerializer,ImportantDateSerializer,EligibilityCriteriaSerializer
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
                     "internshipDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else {"data":"data unavailable"},
                     "certificationDetails":CertificationSerializer(certificationDetails,many=True).data if certificationDetails.exists() else {"data":"data unavailable"},
                     "token":token.key,
                     "user":serializer.data,
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
        user = Token.objects.get(key=token).user
        serializer = UserSerializer(instance=user)
        student = Student.objects.filter(roll_number=user.username).first()
        internships = Internship.objects.filter(roll_number=user.username)
        certifications = Certification.objects.filter(roll_number=user.username)
        return Response({
            "studentDetails": StudentSerializer(student, many=False).data if student else {"data": "data unavailable"},
            "internshipDetails": InternshipSerializer(internships, many=True).data if internships.exists() else {"data": "data unavailable"},
            "certificationDetails": CertificationSerializer(certifications, many=True).data if certifications.exists() else {"data": "data unavailable"},
            "token": token,
            "user": serializer.data,
        })
    except Token.DoesNotExist:
        return Response({"details": "not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def getJobPost(request):
    try:
        JobPosts = Jobs.objects.all()
        serealizer = JobSerializer(JobPosts,many=True)
        for job in serealizer.data:
            print('job :',job['id'],job['Title'])
            imp_dates = ImportantDates.objects.filter(Job = job['id'])  
            criteria = EligibilityCriteria.objects.filter(job=job['id']).first()
            if imp_dates.exists():
                job['importantDates'] = ImportantDateSerializer(imp_dates,many=True).data
            else:
                job['importantDates'] =    "unaivailable"
            if criteria:
                job['EligibilityCriteria'] = EligibilityCriteriaSerializer(instance=criteria).data
            else:
                job['EligibilityCriteria'] = "unaivailable"
        return Response(serealizer.data)
    
    except Exception as e:
        print(str(e))
        return Response({"err_details": str(e)}, status=status.HTTP_404_NOT_FOUND)

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
                     "internshipDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else {"data":"data not found"},
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
    

@api_view(["POST"])
def uploadIntern(request):
    serializer = InternshipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)