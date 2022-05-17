from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from main.models import (Application, User , Student)


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self ):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user) 
        return user

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('reviewed','approved', 'scholarship_type',)
    
    def save(self):
        print(self.cleaned_data)
        application = Application.objects.create(**self.cleaned_data) 
        return application
    