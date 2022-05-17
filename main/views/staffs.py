from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import staff_required
from ..forms import ApplicationForm, StudentSignUpForm 
from ..models import Application 

@method_decorator([login_required, staff_required], name='dispatch')
class ViewScholarshipSubmission(ListView):
    model = Application
    ordering = ('name', )
    context_object_name = "Application"
    template_name = 'main/staffs/application_list.html'

    def get_queryset(self):
        queryset = Application.objects.all()
        return queryset
    



