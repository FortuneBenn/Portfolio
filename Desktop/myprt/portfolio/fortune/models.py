from django.db import models
from datetime import date

# Create your models here.

class Details(models.Model):
    firstname = models.CharField(max_length=15, blank=False)
    middlename = models.CharField(max_length=15, blank=False)
    surname = models.CharField(max_length=15, blank=False)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    race = models.CharField(max_length=15, blank=False)
    #id_no = models.CharField(max_length=13, blank=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)

    def calculate_age(self):
        today = date.today()
        if self.date_of_birth:
            age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            return age
        return None

class Skill(models.Model):
    skill = models.CharField(max_length=20, blank=True, null=True)
    skill_percentage = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

class WorkExperience(models.Model):
    position = models.CharField(max_length=20, blank=True, null=True)
    job_decription = models.CharField(blank=True,  null=True, max_length=200)
    company = models.CharField(max_length=100, blank=True, null=True)
    company_link = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True,null= True)
    end_date = models.DateField(blank=True,null= True)

class Education(models.Model):
    qualification = models.CharField(blank=True,  null=True, max_length=200)
    qualification_discription = models.CharField(blank=True,  null=True, max_length=200)
    institution = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True,null= True)
    end_date = models.DateField(blank=True,null= True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/images/', null=True, blank=True)
    gif = models.FileField(upload_to='projects/gifs/', null=True, blank=True)
