from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class User1Profile(models.Model):
    address = models.CharField(blank=True, max_length=300)
    city = models.CharField(blank=True, max_length=40)
    state = models.CharField(blank=True, max_length=50)
    pin_code = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

class User2Profile(models.Model):
    phone = models.CharField(blank=True, max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '
