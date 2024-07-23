# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from .views import Userviewset

# router = DefaultRouter()  
# router.register('',Userviewset,basename='user')     
# app_name = 'user'

# urlpatterns = [
#     path('',include(router.urls))
# ]


from django.urls import path
from .views import ManageUserView, RegisterUserAPIView

app_name = 'user'

urlpatterns = [
    path('register',RegisterUserAPIView.as_view()),
    path('me',ManageUserView.as_view(),name="me")
]