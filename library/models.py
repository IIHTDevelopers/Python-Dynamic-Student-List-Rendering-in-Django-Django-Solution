from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)
    roll_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
