from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectFormView.as_view(), name='main'),
]
