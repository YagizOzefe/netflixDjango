from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 20)
    slug = AutoSlugField(populate_from = 'title',unique = True)

    def __str__(self):
        return self.title
    

class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='movies/')
    video = models.FileField(upload_to='movies/')
    description = models.TextField(blank = True,null = True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title