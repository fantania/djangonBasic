from django.urls import path
from . import views 

urlpatterns = [
    path('<int:pk>', views.employees_detail) #the primary key -> pk can be any name
]