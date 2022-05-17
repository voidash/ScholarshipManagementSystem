from django.urls import include, path

from .views import scholarship, staffs, students 


urlpatterns = [
    path('', scholarship.home ,name = 'home' ),
    path('students/', include((
            [
                path('', students.ViewScholarships.as_view(), name='view_scholarships'),
                path('apply/<int:pk>/', students.SubmitScholarshipApplication, name='apply_scholarship'),
                path('description/<int:pk>/', students.ShowDescription, name='scholarship_description'),
                path('applied_scholarships/', students.ViewSubmittedScholarships.as_view(), name='applied_scholarship'),
            ], 'sms'
    ), namespace='students'
    ))
]