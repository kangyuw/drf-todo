from rest_framework import generics
from .models import Todo, Task
from .serializers import TaskSerializers, TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ItemTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TaskList(generics.ListAPIView):
    model = Task
    serializer_class = TaskSerializers
    def get_queryset(self):
            todo_id = self.kwargs['id']
            return Task.objects.filter(todo_id=todo_id)