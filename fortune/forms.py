from django import forms
from .models import Contact  # Import the Contact model from your app's models

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

