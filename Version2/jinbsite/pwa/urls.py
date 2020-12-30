from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('projects',views.projects, name="Projects"),
    path('resources',views.resources, name="Resources"),
    path('contact',views.contact, name="Contact"),
]