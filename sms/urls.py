from django.contrib import admin
from django.urls import path, include

from main.views import scholarship, students

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('main.urls')),
    path('teams/', scholarship.team),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
]
