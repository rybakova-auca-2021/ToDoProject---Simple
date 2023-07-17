from django.urls import path, include
from .views import toDoAppView, addToDoView

urlpatterns = [
    path('list/', toDoAppView, name='list'),
    path('addItem/', addToDoView, name='addItem'), 
]