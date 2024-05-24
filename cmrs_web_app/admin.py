from django.contrib import admin
from import_export import resources
from .models import Student,Internship,TPODetails,Project,Certification,Jobs,Company,ImportantDates,StudentFeedback,Branch,EligibilityCriteria,Application
from import_export.admin import ImportExportModelAdmin

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = True
        exclude = ['id']
        import_id_fields = ['roll_number']

class StudentAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','name','email','branch','batchYear']
    resource_class = StudentResource
    search_fields = ['roll_number','name','email']
    list_filter = ['batchYear','branch']
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ['name','id']

class JobsAdmin(ImportExportModelAdmin):
    list_display = ['Title','id','Description']
    search_fields = ['Title','Company']
    list_filter = ['Location','JobType']

class CompanyAdmin(ImportExportModelAdmin):
    search_fields = ['Name','Location','Industry']

class InternshipAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','company_name','role','start_date','end_date','responsibilities']
    search_fields = ['roll_number__name','company_name__Name']

class ProjectAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','title','description','technologies_used','github_repo_url']
    search_fields = ['roll_number__name','title','technologies_used']

class CertificationAdmin(ImportExportModelAdmin):
    list_display = ['roll_number','title','year_earned','url','skills','domain_technology']
    search_fields = ['roll_number__name','title','skills','domain_technology']

class EligibilityCriteriaAdmin(ImportExportModelAdmin):
    list_display = ['job','min_cgpa','max_backlog_count','skills_required','min_twelth_percentage','min_tenth_cgpa','no_gap_year']
    search_fields = ['job__Title']

class ApplicationAdmin(ImportExportModelAdmin):
    list_display = ['student','job','branch','batchYear','is_accepted']
    search_fields = ['student__name','job__Title']
    list_filter = ['batchYear','branch','status','is_accepted']
#Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Jobs,JobsAdmin)
admin.site.register(EligibilityCriteria,EligibilityCriteriaAdmin)
admin.site.register(ImportantDates)
admin.site.register(Application,ApplicationAdmin)
admin.site.register(StudentFeedback)
admin.site.register(TPODetails)
admin.site.register(Student,StudentAdmin)
admin.site.register(Branch)
admin.site.register(Internship,InternshipAdmin)
admin.site.register(Project,ProjectAdmin) 
admin.site.register(Certification,CertificationAdmin)