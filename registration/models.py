from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=30, default='Guest')
    phone_num = models.BigIntegerField(unique=True)
    joining_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=30, default='Pune')

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['role']