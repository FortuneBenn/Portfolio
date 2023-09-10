from django.shortcuts import render
from .models import Skill, WorkExperience, Education, Details, Project

# Create your views here.
def resume(request):
    details = Details.objects.first()  # Assuming you have only one Details object
    skills = Skill.objects.all()
    work_experiences = WorkExperience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all()

    context = {
        'details': details,
        'skills': skills,
        'work_experiences': work_experiences,
        'educations': educations,
        'projects': projects,
    }

    return render(request, 'portfolio/resume.html', context)