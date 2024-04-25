from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('signup',views.userSingup),
    path('login',views.userLogin),
    path('checklogin',views.userAuthenticate),
    path('getjobs',views.getJobPost),
    path('getcomplist',views.sendCompanyList),
    path('resbybranch',views.sendResultByBranch),
    path('resbyjob',views.sendProfileByJob),
    path('getstudentprofile',views.sendProfile),
    path('getbranchprofiles',views.sendAllProfiles),
    path('getbranch',views.getBranches),
    path('uploadCert',views.uploadCert),
    path('uploadIntern',views.uploadIntern),
]
