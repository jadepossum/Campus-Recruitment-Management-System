from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('singup',views.userSingup),
    path('login',views.userLogin),
    path('checklogin',views.userAuthenticate),
    path('getjobs',views.getJobPost),
    path('profile',views.sendProfile),
    path('uploadCert',views.uploadCert),
]
