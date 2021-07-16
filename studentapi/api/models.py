from django.db import models


class Institute(models.Model):
    C=(('s','school'),('c','college'))
    name=models.CharField(max_length=100)
    institute=models.CharField(max_length=1,choices=C)
    def __str__(self):
        return self.name


class Student(models.Model):
    G=(('f','female'),('m','male'),('u','undisclosed'))
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=1,choices=G)
    percentage=models.FloatField()
    inst=models.ForeignKey('Institute',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.name




