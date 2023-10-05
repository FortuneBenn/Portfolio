from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name="home-page"),
    path('resume', views.resume, name="resume-page"),
    path('projects', views.projects, name="projects-page"),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('contact/', views.contact_form, name='contact_form'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)