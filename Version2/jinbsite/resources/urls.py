from django.urls import path
from . import views


urlpatterns = [

    path('',views.resource, name="Resources"),
    path('category/<int:category_id>/', views.category, name="category"),

]