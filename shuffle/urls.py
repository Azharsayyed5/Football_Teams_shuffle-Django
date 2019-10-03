from django.urls import path,include
from shuffle import views

urlpatterns = [
    path('Index/',views.test),
    path('demo/',views.showallteams),
    
]
