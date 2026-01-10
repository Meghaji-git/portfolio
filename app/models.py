from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Services(models.Model):
    domain = models.CharField(max_length=100,blank=True,null=True)
    disciption = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.domain

class Projects(models.Model):
    project_name = models.CharField(max_length=30,blank=True,null=True)
    disciption = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to="media",blank=True,null=True)
    url = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.project_name

    