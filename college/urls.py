from django.urls import path
from college import views

urlpatterns = [
    path('', views.index, name='index'),
]