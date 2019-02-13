from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.last_name + ' - ' + self.message