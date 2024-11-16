from django.db import models


class Utilisateur(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default="youssef@gmail.com",unique=True)
    password = models.CharField(max_length=100)



class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    service = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Article(models.Model):
    description = models.TextField(max_length=200)
    titre= models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titre
