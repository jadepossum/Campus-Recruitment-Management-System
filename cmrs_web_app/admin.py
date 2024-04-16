from django.contrib import admin
from import_export import resources
from .models import Student,Internship,Project,Certification,Jobs,Company,ImportantDates,StudentFeedback,Branch,EligibilityCriteria
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

class EligibilityCriteriaAdmin(ImportExportModelAdmin):
    list_display = ['job','min_cgpa','max_backlog_count','skills_required','min_twelth_percentage','min_tenth_cgpa','no_gap_year']

#Register your models here.
admin.site.register(Jobs,JobsAdmin)
admin.site.register(Company)
admin.site.register(EligibilityCriteria,EligibilityCriteriaAdmin)
admin.site.register(ImportantDates)
admin.site.register(StudentFeedback)
# admin.site.register(UserLogin)


admin.site.register(Student,StudentAdmin)
admin.site.register(Branch)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Project,ProjectAdmin) 
admin.site.register(Certification,CertificationAdmin)