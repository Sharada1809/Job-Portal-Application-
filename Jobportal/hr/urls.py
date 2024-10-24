from django.urls import path
from hr import views
app_name='hr'

urlpatterns = [
    path('hrdash/',views.hrHome,name='hrHome'),
    path('candidatedetails/<int:id>/',views.hrCandidateDetails,name='hrCandidateDetails'),
    path('postjob/',views.postJobs,name='postJobs'),
    path('acceptapplication/',views.acceptApplication,name='acceptApplication'),
    path('hrnavbar/',views.hrnavbar,name='hrnavbar')
     
]
