from django.db import models
from django.core.validators import RegexValidator

#custom Fields
class RollNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['validators'] = [RegexValidator(r'^\d{2}JJ[15]A\d{4}$')]
        super().__init__(*args, **kwargs)

# Create your models here.
class Jobs(models.Model):
    Title = models.CharField(("Title"), max_length=50)
    id = models.IntegerField(("ID"), primary_key=True)
    Description = models.CharField(("Desc"),max_length=500, null=True)

    def __str__(self):
        return self.Title

    
class Student(models.Model):
    roll_number = RollNumberField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cgpa = models.FloatField(null = True)
    skills = models.CharField(max_length=250,null = True)
    twelthPercentage = models.FloatField(null = True)
    tenthCGPA = models.FloatField(null = True)
    BackLogCount = models.IntegerField(null = True)
    Gap = models.BooleanField(null = True)
    github_profile = models.URLField(max_length=200, null=True, blank=True)
    linkedin_profile = models.URLField(max_length=200, null=True, blank=True)
    portfolio_website = models.URLField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # resume = models.FileField(upload_to='resumes/')
    def __str__(self):
        return self.name

class UserLogin(models.Model):
    name = models.CharField(("Name"), max_length=50)
    roll_no = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    password = models.CharField(max_length=30,null=True)
    id = models.IntegerField(("ID"), primary_key=True)

    def __str__(self):
        return self.name

class Internship(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.TextField(null=True)

class Project(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    github_repo_url = models.URLField(blank=True)

class UserDefinedTable(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    context = models.TextField()

    def __str__(self):
        return self.title
    
# class Internship(models.Model):
#     organization_name = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)
#     duration_from = models.DateField()
#     duration_to = models.DateField()

class Certification(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    skills = models.CharField(max_length=200)
    domain_technology = models.CharField(max_length=100)
    year_earned = models.DateField()