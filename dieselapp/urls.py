from django.urls import path
from . import views
""" URL configuration for dieselapp app. """
urlpatterns = [
    path('sensor-data/', views.DieselDataList.as_view(), name='dieseldatalist'),
    path('sensor-data/<int:pk>/', views.DieselDataDetail.as_view(), name='dieseldatadetail'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),

]
