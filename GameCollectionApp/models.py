from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class CollectorModel(models.Model):
    username = models.CharField(max_length=200, default="")
    password1 = models.CharField(max_length=200, default="")
    password2 = models.CharField(max_length=200, default="")
    dateAccountCreated = models.DateField(default= timezone.now)
    rank = models.CharField(max_length=200, default="Grunt")
    foreignkeyToUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "This collector is: " + str(self.username)


class GameModel(models.Model):
    name = models.CharField(max_length=200, default="")
    developer = models.CharField(max_length=200, default="")
    dateMade = models.DateField(default = "")
    ageLimit = models.IntegerField(default= 0)
    foreignKeyToCollector = models.ForeignKey(CollectorModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "The game name is: " + str(self.name)
