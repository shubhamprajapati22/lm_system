from django.db import models
from django.contrib.auth.models import User


class StudentInfo(models.Model):
    libid = models.CharField(max_length = 10)
    roll_no = models.BigIntegerField(primary_key = True)
    course = models.CharField(max_length = 5)
    sem = models.IntegerField()
    section = models.CharField(max_length = 4)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
