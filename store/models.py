from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class UserAccount(models.Model):
    username = models.CharField(max_length=150, primary_key=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username
