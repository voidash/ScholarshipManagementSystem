from re import S
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import student_required
from ..forms import ApplicationForm,StudentSignUpForm
from ..models import Scholarship, Student, Application, User

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm 
    template_name= 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] ='student'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students:view_scholarships')

class ViewScholarships(ListView):
    model = Scholarship
    context_object_name = 'Scholarship'
    template_name = 'main/students/scholarships_list.html'

    def get_queryset(self):
        queryset = Scholarship.objects.all()
        return queryset

def ShowDescription(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    return render(request,'main/students/scholarship_description.html', {'scholarship': scholarship})

def SubmitScholarshipApplication(request, pk):
    scholarship = get_object_or_404(Scholarship, pk=pk)
    student = request.user.student
    if request.method == 'POST':
        form = ApplicationForm(request.POST,request.FILES)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            form.cleaned_data['scholarship_type'] = scholarship
            student.applications.add(form.save())
        else:
            return render(request, 'main/students/application_form.html', {'scholarship': scholarship, 'form': form, 'errors': form.errors})


        return redirect('students:view_scholarships')
    else: 
        form = ApplicationForm(initial={'scholarship_type': scholarship})
    

    return render(request, 'main/students/application_form.html', {'scholarship': scholarship, 'form': form})

class ViewSubmittedScholarships(ListView):
    model = Application
    context_object_name = 'Applications'
    template_name = 'main/students/submitted_application.html'


    def get_queryset(self):
        data = self.request.user
        student = Student.objects.get(user=data)
        return student.applications.all()
