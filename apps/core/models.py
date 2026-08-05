from django.db import models

# Create your models here.


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    address = models.TextField()

    # created_at = models.models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Branch(BaseModel):

    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="branches")
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.name}"


class Department(BaseModel):
    branch =  models.ForeignKey(Branch, on_delete=models.CASCADE,related_name="departments")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name