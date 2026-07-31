from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import BaseModel

# Create your models here.

class UserRole(models.TextChoices):
    SUPER_ADMIN = "SUPER_ADMIN", "Super_Admin"
    ADMIN = "ADMIN", "Admin"
    HR = "HR", "HR"
    MANAGER = "MANAGER", "Manager"
    ACCOUNTANT = "ACCOUNTANT","Accountant"
    INVENTORY = "INVENTORY","Inventory"
    SALES = "SALES","Sales"
    EMPLOYEE = "EMPLOYEE","Employee"



class User(AbstractUser,BaseModel):
    phone_number = models.CharField(max_length=10,blank=True)
    profile_picture = models.ImageField(upload_to="profiles/",blank= True, null=True)
    role = models.CharField(max_length=30,choices=UserRole.choices,default=UserRole.EMPLOYEE,)


    def __str__(self):
        return self.username