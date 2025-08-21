from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f'Object of class Employee id:{self.id}, name:{self.name}, score:{self.score}'
