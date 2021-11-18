from django.urls import path
from .views import ListTodo, ItemTodo, TaskList

urlpatterns = [
    path('<int:pk>/', ItemTodo.as_view()),
    path('', ListTodo.as_view()),
    path('todo/<int:id>/tasks/', TaskList.as_view())
]
