from django.db import models

class user(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50) 
    email=models.EmailField() 
    phno=models.IntegerField()
    pwd=models.CharField(max_length=50) 
    conpwd=models.CharField(max_length=50) 
    gender=models.CharField(max_length=50)
    class Meta:
        db_table="user"

class picfile(models.Model):
    pname=models.CharField(max_length=50)
    purl=models.ImageField()
    class Meta:
        db_table="picfile"

