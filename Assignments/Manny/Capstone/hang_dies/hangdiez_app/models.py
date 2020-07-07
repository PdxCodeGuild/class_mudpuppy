from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    state = models.CharField(max_length=32) # Creating state
    def __str__(self):
        return self.state
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)  #creating user id
    states = models.ForeignKey(State, on_delete=models.CASCADE, related_name='user_profile')# pulling from state class... linking user profile to state
    zip_code = models.CharField(max_length=5) # saving user zip code
    city = models.CharField(max_length=64) # saving user city


    def __str__(self):
        return self.user.username
    