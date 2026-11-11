from django.db import models
from datetime import *

class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    caption = models.TextField()
    picture = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)

    
class Order(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    books = models.ManyToManyField(Books)
    lend_at = models.DateTimeField()
    bring_at = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)