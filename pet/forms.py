from django import forms
from pet.models import Pet, PET_TYPE

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['type', 'name', 'birthday']
        widgets = {
        	'type': forms.Select(choices=PET_TYPE, attrs = {"class": "form-control"}),
        	'name': forms.TextInput(attrs = {"class": "form-control"}),
        	'birthday': forms.DateInput(attrs = {"class": "form-control"})
        }
