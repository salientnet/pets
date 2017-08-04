from django.db import models
from django.contrib.auth.models import User

PET_TYPE = [('Dog', 'Dog'), ('Cat', 'Cat')]
class Pet(models.Model):
    type = models.CharField("Type", max_length=40, choices=PET_TYPE, default='Dog')
    name = models.CharField("Name", max_length=50, error_messages = { 'required': 'Name is required.' })
    birthday = models.DateField("Birthday",error_messages = {'required': 'Birthday is required.'})
    owner = models.ForeignKey(User)
