from django.urls import path, include
from .views import toDoAppView, addToDoView, deleteItemView

urlpatterns = [
    path('list/', toDoAppView, name='list'),
    path('addItem/', addToDoView, name='addItem'), 
    path('deleteItem/<int:i>/', deleteItemView, name='deleteItem')
]