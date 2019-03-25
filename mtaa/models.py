from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    image = models.ImageField(upload_to = 'images/')

    # @classmethod
    # def find_neigborhood(cls,neighborhood_id):
    #     neighborhood=cls.objects.filter(id=neighborhood_id)
    #     return neighborhood
    #
    @classmethod
    def search_by_name(cls,search_term):
        neighborhood=cls.objects.filter(name__icontains=search_term)
        return neighborhood


class Profile(models.Model):
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio=models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class Business(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email=models.EmailField()

class Post(models.Model):
    post=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
