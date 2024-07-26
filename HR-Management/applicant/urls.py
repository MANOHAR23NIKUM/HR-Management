from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Applicantviewset

router = DefaultRouter()  
router.register('',Applicantviewset,basename='applicantion')     
app_name = 'applicant'

urlpatterns = [
    path('',include(router.urls))
]