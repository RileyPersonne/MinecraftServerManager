import datetime

from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Main(models.Model):
    servername = models.CharField(max_length=16)



class Dashboard(models.Model):
    username = models.CharField(max_length=16)