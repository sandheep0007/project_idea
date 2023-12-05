from django.contrib import admin
from .models import Course, Technology,ProjectType,Topic
from django.http import HttpResponse
from reportlab.pdfgen import canvas
#function for pdf converter
class ParentModelSuper(admin.ModelAdmin):
    list_display=('created_user',)
    
    

def make_pdf(cur_class,req,queryset):
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition']='attachment'; filename="project details.pdf"
    pdf=canvas.Canvas(response)
    #fetch model values and write them to pdf
    for obj in queryset:
        topicname=obj.topicname
        coursename=obj.coursename
        Technologyname=obj.Technologyname
        description=obj.description
        created_user=obj.created_user    
        project_type=obj.project_type

        #write atribute values

        pdf.drawString(200,800,f"project details")   
        pdf.drawString(200,770,f"project title: {topicname}")   
        pdf.drawString(200,750,f"created user: {created_user}")   
        pdf.drawString(200,730,f"course: {coursename}")   
        pdf.drawString(200,600,f"project type: {project_type}")   
        pdf.drawString(200,680,f"technology: {Technologyname}")   
        pdf.drawString(200,660,f"description: {description}")
        #move to the next page
        pdf.showPage()    
        #close pdf canvas
        pdf.save()
    return response
make_pdf.short_description="export to pdf"

class Exporttopic(ParentModelSuper):
    list_display = ParentModelSuper.list_display + (
        'coursename', 'project_type', 'description', 'Technologyname', 'topicname')
    actions=[make_pdf]
    
# class TechnologyAdmin(ParentModelSuper):
#     list_display=['Technologyname']
#     exclude=['created_user']



class CourseAdmin(admin.ModelAdmin):
    exclude =['created_user']











admin.site.register(Course,CourseAdmin)
admin.site.register(Technology)
admin.site.register(ProjectType)
admin.site.register(Topic,Exporttopic)


































