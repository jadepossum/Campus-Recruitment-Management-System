from django.contrib import admin
from import_export import resources
from .models import Jobs,UserLogin,Student,Internship,Project,Certification
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = True
        exclude = ['id']
        import_id_fields = ['roll_number']

class StudentAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','name','email']
    resource_class = StudentResource

# class UsersAdmin(admin.ModelAdmin):
#     list_display = ['name','id']

class JobsAdmin(ImportExportModelAdmin):
    list_display = ['Title','id','Description']

class InternshipAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','company_name','role','start_date','end_date','responsibilities']

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','title','description','technologies_used','github_repo_url']

class CertificationAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','title','url','skills','domain_technology','year_earned']

#Register your models here.
admin.site.register(Jobs,JobsAdmin)
admin.site.register(UserLogin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Project,ProjectAdmin) 
admin.site.register(Certification,CertificationAdmin)