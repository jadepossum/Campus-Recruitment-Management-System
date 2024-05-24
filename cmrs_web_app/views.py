from rest_framework import status
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student,Internship,Certification,Jobs,ImportantDates,EligibilityCriteria,Branch,Application,TPODetails,StudentFeedback
from .serializers import UserSerializer,StudentSerializer,InternshipSerializer,CertificationSerializer,JobSerializer,ImportantDateSerializer,EligibilityCriteriaSerializer,StudentBranchSerializer,ApplicationSerializer,FeedBackSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage

# Create your views here.
@api_view(["POST"])
def userLogin(request):
    try:
        username = request.data['username']
        user = get_object_or_404(User, username=username)
    except:
        return Response({"detail":"User is not registered","err":"yes"})
    if not user :
        # return Response({"detail":"User is not registered","err":"yes"},status=status.HTTP_404_NOT_FOUND)
        return Response({"detail":"User is not registered","err":"yes"})
    if not user.check_password(request.data['password']):
        # return Response({"detail":"Password doesn't match","err":"yes"},status=status.HTTP_404_NOT_FOUND)
        return Response({"detail":"Password doesn't match","err":"yes"})
    currentbatchyear = TPODetails.objects.first().CurrentBatchYear
    token ,created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    studentDetails = Student.objects.filter(roll_number = username).first()
    internshipDetails = Internship.objects.filter(roll_number = username)
    certificationDetails = Certification.objects.filter(roll_number = username)
    myApplications = Application.objects.filter(student = username)
    return Response({"studentDetails":StudentSerializer(studentDetails,many=False).data if studentDetails else {"data":"data unavailable"},
                     "internshipDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else {"data":"data unavailable"},
                     "certificationDetails":CertificationSerializer(certificationDetails,many=True).data if certificationDetails.exists() else {"data":"data unavailable"},
                     "token":token.key,
                     "user":serializer.data,
                     "currentBatchYear":currentbatchyear,
                     "myApplications":ApplicationSerializer(myApplications,many=True).data
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
        paginate_by = 20
        JobPosts = Jobs.objects.all().order_by("-PostedDate","-id")
        paginator = Paginator(JobPosts,paginate_by)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        serealizer = JobSerializer(page,many=True)
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
        return Response({"totalPageCount":paginator.num_pages,"currentPage":page_number,"hasNextPage":page.has_next(),"posts" :serealizer.data})
    
    except Exception as e:
        print(str(e))
        return Response({"err_details": str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def getFeedbacks(request):
    eventid = int(request.GET['eventid'])
    feedbacks = StudentFeedback.objects.all()
    resp_list = []
    for feedback in feedbacks:
        if feedback.imp_date.id==eventid:
            resp = {}
            resp["feedback_id"]  = feedback.id
            resp["event"] = feedback.imp_date.EventTitle
            resp["event_id"] = feedback.imp_date.id
            resp["student_name"] = feedback.RollNumber.name
            resp["roll_number"]  = feedback.RollNumber.roll_number
            resp["feedback"]     = feedback.PhaseFeedback
            resp_list.append(resp)
    
    return Response({"feedbacks":resp_list})

@api_view(["POSt"])
def writeFeedback(request):
    event_id = request.data['imp_date']
    roll_number = request.data['RollNumber']
    feedback = StudentFeedback.objects.filter(RollNumber = roll_number,imp_date = event_id).first()
    if feedback :
        feedback.PhaseFeedback = request.data['PhaseFeedback']
        feedback.save()
        return Response({"msg":"feedback updated"})
    
    serializer = FeedBackSerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(["POSt"])
def directApply(request):
    rollNumber = request.data['student']
    jobid = request.data['job']
    application = Application.objects.filter(student=rollNumber,job=jobid).first()
    if application :
        return Response({"msg":"Already Applied"})
    else:
        serializer = ApplicationSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    pass

@api_view(["GET"])
def sendCompanyList(request):
    applications = Application.objects.all()
    resp = {}
    resp_list = []
    for application in applications:
        if(application.is_accepted):
            resp[application.job.__str__()] = application.job.id
    return Response({"company_list":resp.items()})

@api_view(["GET"])
def sendResultByBranch(request):
    branch = request.GET['branch']
    batch = request.GET['batch']
    applications = Application.objects.filter(branch=branch,is_accepted=True,batchYear=batch)
    resp_list =[]
    for appication in applications:
        resp = {}
        resp["student_name"] = appication.student.name
        resp["roll_number"]  = appication.student.roll_number
        resp["jobid"]        = appication.job.id
        resp["role"]         = appication.job.Title
        resp["company_name"] = appication.job.Company
        resp_list.append(resp)
    return Response({"applications":resp_list})

@api_view(["GET"])
def sendProfileByJob(request):
    jobid = request.GET['jobid']
    applications = Application.objects.filter(job=jobid,batchYear=2020)
    resp_list =[]
    for appication in applications:
        if(not appication.is_accepted):
            continue
        resp = {}
        resp["student_name"] = appication.student.name
        resp["roll_number"]  = appication.student.roll_number
        resp["jobid"]        = appication.job.id
        resp["role"]         = appication.job.Title
        resp["company_name"] = appication.job.Company
        resp_list.append(resp)
    return Response({"applications":resp_list})
    
@api_view(["GET"])
def sendProfile(request):
    rollNumber = request.GET['studentid']
    student = Student.objects.filter(roll_number = rollNumber).first()
    internshipDetails = Internship.objects.filter(roll_number = rollNumber)
    certificationDetails = Certification.objects.filter(roll_number = rollNumber)
    return Response({
        "studentDetails":StudentSerializer(student,many=False).data if student else {"data":"data not found"},
        "internshipDetails":InternshipSerializer(internshipDetails,many=True).data if internshipDetails.exists() else [],
        "certificationDetails":CertificationSerializer(certificationDetails,many=True).data if certificationDetails.exists() else [],
    })

@api_view(["GET"])
def sendAllProfiles(request):
    branch = request.GET['branch']
    students = Student.objects.filter(branch=branch,batchYear=2020)
    serializer = StudentBranchSerializer(students,many=True)
    return Response({"studentDetails":serializer.data})

@api_view(["GET"])
def getBranches(request):
    branch = Branch.objects.first()
    return Response({"branchName :",branch.name})

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