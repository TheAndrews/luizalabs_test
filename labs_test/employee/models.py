from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    department = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name