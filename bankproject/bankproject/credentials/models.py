# models.py
from django.db import models


class Login(models.Model):
    uname=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    cpwd = models.CharField(max_length=20)

class Register(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phno = models.CharField(max_length=15)
    mailid = models.EmailField()
    password = models.CharField(max_length=128)  # You should consider using a secure password hashing method.
    address = models.TextField()
    district = models.CharField(max_length=100)
    account_type = models.CharField(max_length=20)
    materials = models.CharField(max_length=255)  # Store selected materials as a comma-separated string

    def __str__(self):
        return self.name



