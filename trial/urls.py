from django.urls import path
from trial import views

urlpatterns = [
    path('', views.trial, name='trial'),
]