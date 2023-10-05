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
    address = models.CharField(max_length=200, unique=True, blank=True,default=' ')
    boi = models.CharField(max_length=500, unique=True, blank=True,default=' ')
    phone_number = models.CharField(max_length=15, blank=False)
    title = models.CharField(max_length=100,blank=True,default=' ')

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
    stack = models.CharField(max_length=300,blank=True,default=' ')

    def __str__(self):
        return self.title

    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name  # This will display the name of the contact in the admin panel

    class Meta:
        verbose_name = 'Contact'  # Singular form for the model name
        verbose_name_plural = 'Contacts'  # Plural form for the model name
