from ast import Delete
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=200) 
    description = models.TextField(null=True, blank=True)
    item_complete = models.BooleanField(default=False)
    create_t_d = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    # class Meta:
    #     ordering = ['complete']