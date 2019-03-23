from django.db import models


class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
