from django.shortcuts import render, redirect
from .forms import ContactForm
import json
from django.http import HttpResponse
from .models import Skill, WorkExperience, Education, Details, Project, Contact

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
def home(request):
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

    return render(request, 'portfolio/index.html', context)
def projects(request):
    projects = Project.objects.all()
    details = Details.objects.first()
    project_list = [(index + 1, project) for index, project in enumerate(projects)]

    context = {
        'projects': projects,
        'details': details,
        'project_list':project_list,
    }

    return render(request, 'portfolio/projects.html', context)

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the Contact model
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save to Contact model
            contact = Contact(name=name, email=email, message=message)
            contact.save()

           

    # Handle form errors or other scenarios here
    return redirect('contact_form')  # Redirect back to the contact form on error

def contact_form(request):
    # Your existing code for rendering the contact form
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


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact object and save it to the database
            contact = form.save()
            # Optionally, you can do additional processing here
            # Redirect to a success page or do any other necessary tasks
            #return redirect('success_page')  # Replace 'success_page' with your actual success page URL
    else:
        form = ContactForm()

    # Render the contact form template with the form
    return HttpResponse(json.dumps(),content_type='application/json')