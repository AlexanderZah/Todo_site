from django.db import models
from django.contrib.auth.models import User

class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,verbose_name='description')
    important = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(null=True, blank=True, verbose_name='time todo this')

    def __str__(self):
        return self.title
    