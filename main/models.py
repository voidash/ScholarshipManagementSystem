from django.db import models


from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


class Scholarship(models.Model):
    scholarship_type = models.CharField(max_length=255)
    application_open_date = models.DateTimeField()
    application_close_date = models.DateTimeField()
    scholarship_field = RichTextField()
    money = models.IntegerField()
    number_of_opening = models.IntegerField()
    scholarship_status = models.TextField()

    def __str__(self):
        return self.scholarship_type 

class Application(models.Model):
    scholarship_type = models.ForeignKey(Scholarship, null=True, blank=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    name = models.CharField(max_length=300)
    permanent_mailing_address = models.TextField()
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField()
    high_school_name = models.TextField()
    high_school_diploma_date = models.DateField()
    high_school_GPA = models.FloatField()
    university_choice = models.TextField()
    major_field_of_study = models.TextField()
    enrolled_to_university = models.BooleanField()
    essay = models.FileField(upload_to="essays/")
    documents = models.FileField(upload_to="documents/")

    def __str__(self):
        if self.scholarship_type :
            return  self.scholarship_type.scholarship_type +  " -->  " + self.name
        else:
            return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    applications = models.ManyToManyField(Application)
    #scholarships =


