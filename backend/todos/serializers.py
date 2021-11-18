from rest_framework import serializers
from .models import Todo, Task

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body',)

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'body', 'todo_id')