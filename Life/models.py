from django.db import models

# Create your models here.

class Department(models.Model):
    Dept_id=models.IntegerField(primary_key=True)
    Dept_name=models.CharField(max_length=100)
    Dept_loc=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Dept_name

class Employee(models.Model):
    Emp_id = models.IntegerField(primary_key=True)
    Emp_name = models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Manager=models.IntegerField()
    Hire_date=models.DateField()
    Salary=models.IntegerField()
    Dept_id=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Emp_name