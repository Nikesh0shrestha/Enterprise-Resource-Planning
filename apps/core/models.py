from django.db import models

# Create your models here.


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name