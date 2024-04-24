
from typing import Iterable
from django.db import models
from django.core.validators import RegexValidator
import datetime


#custom Fields
class RollNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['validators'] = [RegexValidator(r'^\d{2}JJ[15]A\d{4}$')]
        super().__init__(*args, **kwargs)

# Create your models here.
# class Jobs(models.Model):
#     Title = models.CharField(("Title"), max_length=50)
#     id = models.IntegerField(("ID"), primary_key=True)
#     Description = models.TextField(("Desc"), null=True)
#     Prerequisites = models.TextField(null=True)
#     RequiredSkills = models.TextField(null=True)
#     Salary = models.PositiveIntegerField(null=True)
#     Location = models.CharField(max_length=50, null=True)
#     Status = models.CharField(max_length=50, choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN')
#     Deadline = models.DateField(null=True)
#     class Meta:
#         ordering = ['-id']

class Jobs(models.Model):
    Title = models.CharField(("Title"), max_length=50)
    id = models.IntegerField(("ID"), primary_key=True)
    Description = models.TextField(("Desc"), null=True)
    Prerequisites = models.TextField(null=True)
    RequiredSkills = models.TextField(null=True)
    Salary = models.PositiveIntegerField(null=True)
    Location = models.CharField(max_length=50, null=True)
    Status = models.CharField(max_length=50, choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='OPEN')
    Deadline = models.DateField(null=True)
    Company = models.CharField(max_length=50, null=True)  # The company offering the job
    JobType = models.CharField(max_length=50, choices=[('FT', 'Full Time'), ('PT', 'Part Time'), ('IN', 'Internship')], null=True)  # The type of job (Full Time, Part Time, Internship)
    ExperienceLevel = models.CharField(max_length=50, choices=[('EN', 'Entry Level'), ('IN', 'Intermediate'), ('EX', 'Experienced')], null=True)  # The experience level required for the job
    PostedDate = models.DateField(default=datetime.date(2023, 12, 12))  # The date the job was posted
    ApplyLink = models.URLField(max_length=200, null=True)
    def __str__(self):
        return self.Title + " | " + self.Company

class Company(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Industry = models.CharField(max_length=100)
    Size = models.IntegerField()  # Number of employees
    Description = models.TextField(null=True)
    FoundedDate = models.DateField(null=True)
    Website = models.URLField(max_length=200, null=True)

    # def __str__(self):
    #     return self.Name


class ImportantDates(models.Model):
    Job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    Date = models.DateField()
    Description = models.CharField(max_length=250)
    EventTitle = models.CharField(max_length=250)
    # Attendance = models.BooleanField(default=False)
    # Student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return self.EventTitle + " - " + Jobs.objects.get(id=self.Job.id).Title
    class meta:
        unique_together = ('Job', 'Date')
        ordering = ['Job','-Date']

class StudentFeedback(models.Model):
    imp_date = models.ForeignKey(ImportantDates, on_delete=models.CASCADE)
    RollNumber = models.ForeignKey('Student', on_delete=models.CASCADE)
    PhaseFeedback = models.TextField(null=True)
    Rating = models.IntegerField(null=True)  # A rating out of 5 or 10 for the phase

    class Meta:
        unique_together = ('imp_date', 'RollNumber',)
        ordering = ['-imp_date', 'RollNumber']  # Ensures a student can only give feedback once for each phase of a job

    def __str__(self):
        return self.RollNumber.name + " - " + str(self.imp_date)

class Branch(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('IT', 'IT'),
        ('ME.', 'ME'),
        ('ECE', 'ECE'),
    ]
    name = models.CharField(max_length=100, choices=BRANCH_CHOICES)
    departmentHead = models.CharField(max_length=100)
    def __str__(self):
        return self.get_name_display()
    
class Student(models.Model):
    roll_number = RollNumberField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cgpa = models.FloatField(null = True)
    skills = models.CharField(max_length=250,null = True)
    twelthPercentage = models.FloatField(null = True)
    tenthCGPA = models.FloatField(null = True)
    BackLogCount = models.IntegerField(null = True)
    github_profile = models.URLField(max_length=200, null=True, blank=True)
    linkedin_profile = models.URLField(max_length=200, null=True, blank=True)
    portfolio_website = models.URLField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male')
    BRANCH_CHOICES = [
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('IT', 'IT'),
        ('ME.', 'ME'),
        ('ECE', 'ECE'),
    ]
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default='CSE')
    batchYear = models.IntegerField(default=2024)
    year_gap = models.BooleanField(default=False)
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # resume = models.FileField(upload_to='resumes/')
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs) -> None:
        batch = int(self.roll_number[0:2])
        discipline = self.roll_number[4]
        Branch_code = int(self.roll_number[6:8])
        branchlist = {5: "CSE", 2: "EEE", 12: "IT", 3: "ME", 4: "ECE"}
        if discipline == '1' :
            self.batchYear = 2000 + batch
        else :
            self.batchYear = 2000 + batch - 1
        if Branch_code in branchlist:
            self.branch = branchlist[Branch_code]
        return super().save(*args,**kwargs)
    

class EligibilityCriteria(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    min_cgpa = models.FloatField(default=7.0)
    max_backlog_count = models.IntegerField(default=0)
    skills_required = models.CharField(max_length=250, blank=True,null=True)
    min_twelth_percentage = models.FloatField(null=True,default=80)
    min_tenth_cgpa = models.FloatField(null=True,default=7.0)
    no_gap_year = models.BooleanField(default=True)
    def __str__(self):
        return self.job.Title+ " | " + self.job.Company

class Application(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    branch = models.CharField(max_length=5,default="CSE")
    batchYear = models.IntegerField(default=2020)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('APPLIED', 'Applied'), ('REJECTED', 'Rejected'), ('ACCEPTED', 'Accepted')], default='APPLIED')
    is_accepted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student.name} - {self.job.Title}"
    class Meta:
        ordering = ['-job','-application_date']
    def save(self,*args, **kwargs) -> None:
        rollNumber = self.student.roll_number
        batch = int(rollNumber[0:2])
        discipline = rollNumber[4]
        Branch_code = int(rollNumber[6:8])
        branchlist = {5: "CSE", 2: "EEE", 12: "IT", 3: "ME", 4: "ECE"}
        if discipline == '1' :
            self.batchYear = 2000 + batch
        else :
            self.batchYear = 2000 + batch - 1
        if Branch_code in branchlist:
            self.branch = branchlist[Branch_code]
        return super().save(*args, **kwargs)



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
    
class Certification(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField()
    skills = models.CharField(max_length=200)
    domain_technology = models.CharField(max_length=100)
    year_earned = models.DateField()

class TPODetails(models.Model):
    Name  = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    CurrentBatchYear = models.IntegerField()

    def __str__(self):
        return self.Name + " | TPO"