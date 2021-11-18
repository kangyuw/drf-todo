from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"{self.id} {self.title}"

class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)