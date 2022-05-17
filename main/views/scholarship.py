from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('staffs:view_scholarship_submission')
        else:
            return redirect('students:view_scholarships')
    return render(request, 'main/home.html')

def team(request):
    return render(request, 'team.html')