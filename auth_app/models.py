from django.db import models


class Utilisateur(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default="youssef@gmail.com",unique=True)
    password = models.CharField(max_length=100)


    