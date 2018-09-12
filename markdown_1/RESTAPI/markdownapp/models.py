from django.db import models


# Create your models here.
class Note(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
