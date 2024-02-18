from django.urls import path
from .views import CreateToDoView

urlpatterns = [
    path('createToDo',CreateToDoView.as_view(),name='create_todo'),
    path('getToDos',CreateToDoView.as_view(),name='get_todos'),
    path('updateToDo/<int:pk>',CreateToDoView.as_view(),name='update_todo'),
    path('deleteToDo',CreateToDoView.as_view(),name='delete_todo'),
    #path('deleteAll',CreateToDoView.as_view(),name='delete_all'),
]