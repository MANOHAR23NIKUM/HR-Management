from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Attendanceviewset

router = DefaultRouter()  
router.register('',Attendanceviewset,basename='attendance')     
app_name = 'attendance'

urlpatterns = [
    path('',include(router.urls))
]