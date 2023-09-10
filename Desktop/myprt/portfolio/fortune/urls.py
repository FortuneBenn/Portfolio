from . import views
from django.urls import path


urlpatterns = [
    path('resume', views.resume, name="resume-page"),
    
    
]