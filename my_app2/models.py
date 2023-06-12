from django.db import models

# Create your models here.
class person(models.Model):
    gender=[
        ("m","male"),
        ("f","female"),
        ("o","others"),
    ]
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField(default=0,null=True)
    email=models.EmailField()
    gender=models.CharField(max_length=1,choices=gender)
