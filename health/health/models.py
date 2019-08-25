from django.db import models

class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    number=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

