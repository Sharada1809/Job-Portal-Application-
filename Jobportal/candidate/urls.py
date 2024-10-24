from django.urls import path
from candidate import views
app_name='candidate'

urlpatterns = [
     path('dash/',views.candidateHome,name='candidateHome'),
     path('applyjob/<int:id>/',views.applyJob,name='applyJob'),
     path('applylist/',views.myjoblist,name='mylist'),
     path('cnavbar/',views.cnavbar,name='cnavbar'),
     
]
