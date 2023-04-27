from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=10)
    year=models.IntegerField(default=1)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    CGPA = models.IntegerField(default=0)
    
   
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    date_of_admission = models.CharField(max_length=10)
    year_of_graduation = models.IntegerField(default=1)
    
    

