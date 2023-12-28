from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    phone=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    dpartment = models.ForeignKey(Department,on_delete=models.CASCADE)
    
    
    
    
    # date=models.DateField()

    def __str__(self) -> str:
        return self.First_name

