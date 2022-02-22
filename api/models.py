from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    classes = models.CharField(max_length=100)
    dob = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name