from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=350)
    price = models.IntegerField()
    book_image = models.ImageField(default='default.jpg', upload_to='images/')
