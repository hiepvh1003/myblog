from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return self.title

