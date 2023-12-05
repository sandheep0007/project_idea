from django.db import models
from django.contrib.auth.models import User
from abc import ABC, abstractmethod
from django.contrib import admin

class Master(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    isactive=models.BooleanField(default=True,verbose_name="Active")
    created_user=models.ForeignKey(User ,null=True,blank=True,on_delete=models.CASCADE)
    class Meta:
        abstract=True
        ordering=['-isactive']

class Course(Master):
    coursename=models.CharField(max_length=200)

    def __str__(self):
        return self.coursename
    
class Technology(Master):
    Technologyname=models.CharField(max_length=200)
    def __str__(self):
        return self.Technologyname
# project_type_choices=[
#     ('1','mini'),
#     ('2','main'),
#     ('3','live_project')
# ]
class ProjectType(Master):
     project_type = models.CharField(max_length=200)
     def __str__(self):
         return self.project_type
         
    
class Topic(Master):
    coursename=models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE) 
    Technologyname=models.ForeignKey(Technology,null=True,on_delete=models.CASCADE) 
    topicname=models.CharField(max_length=150)
    project_type=models.ForeignKey(ProjectType,null=True,on_delete=models.CASCADE)
    description=models.TextField()
    def __str__(self):
        return self.topicname
    

# Register your models here.
# class PersonAdmin(Master):
#     admin.action(description='Generate PDF file')
#     def generatePDF(modeladmin, request, queryset):
#         url ='templates/admin/person/?pks=' + ','.join(str([q.pk for q in queryset]))
       
#     actions = [generatePDF]

# admin.site.register(Person, PersonAdmin)    
