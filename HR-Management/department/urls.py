from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Departmentviewset

router = DefaultRouter()  
router.register('',Departmentviewset,basename='department')     
app_name = 'department'

urlpatterns = [
    path('',include(router.urls))
]