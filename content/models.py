from django.db import models

class Skill(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to="static/images")
    repository = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.name} - ({self.year})"
    
class Experience(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Default Title')
    description = models.TextField()
    period = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name