from django.db import models

class TodoList(models.Model):
    desc = models.CharField(max_length=150)
