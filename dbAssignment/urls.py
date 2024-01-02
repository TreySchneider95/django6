from django.urls import path
from dbAssignment import views

urlpatterns = [
    path('', views.home, name='home')
]