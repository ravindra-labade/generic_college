from django.db import models


class College(models.Model):
    college_name = models.CharField(max_length=20)
    college_address = models.CharField(max_length=20)
    principal = models.CharField(max_length=20)
    total_students = models.IntegerField()
    total_teachers = models.IntegerField()


