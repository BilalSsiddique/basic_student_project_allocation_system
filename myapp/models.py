from django.db import models

# Create your models here.


class Project(models.Model):
    projectname = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.projectname


class Employee(models.Model):
    projectid = models.ForeignKey(Project, on_delete=models.CASCADE)
    eid = models.CharField(max_length=50)
    ename = models.CharField(max_length=50)
    email = models.EmailField()
    econtact = models.CharField(max_length=50)

    def __str__(self):
        return self.ename
