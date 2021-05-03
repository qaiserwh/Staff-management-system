
from django.contrib.admin.filters import SimpleListFilter
from django.db import models

# Create your models here.
class Degree(models.Model):
    degree_name=models.CharField(max_length=200, db_index=True)

    def __str__(Self):
        return Self. degree_name

class Employ(models.Model):
    name =models.CharField(max_length=550)
    age =models.IntegerField()
    photo =models.ImageField(upload_to='photos')
    salary =models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50,null=True)
    Email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=50)
    Departments=models.CharField(max_length=50)
    Degree =models.ForeignKey(Degree, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name


class Vacation(models.Model):
    employ_name=models.ForeignKey(Employ, on_delete=models.PROTECT)
    title=models.CharField(max_length=250)
    start_date=models.DateField()
    end_date=models.DateField()
    purpose=models.TextField(max_length=500)

    def __str__(Self):
        return Self. purpose

        
class Attendance(models.Model):
    status_employ=[
        ('Absence','Absence'),
        ('Existing','Existing')
    ]
    name_employ=models.ForeignKey(Employ, on_delete=models.PROTECT)
    status =models.CharField(max_length=50,choices=status_employ)
    date=models.CharField(max_length=50,null=True)

    def __str__(Self):
        return Self.status




class Training(models.Model):
    names=models.ForeignKey(Employ, on_delete=models.PROTECT)
    title=models.CharField(max_length=250)
    description=models.TextField()


    def __str__(Self):
        return Self.title

