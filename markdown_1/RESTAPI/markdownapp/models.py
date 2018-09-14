from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Note(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)
    author = models.ForeignKey(User, related_name='all_my_notes', on_delete=models.PROTECT)

    def __str__(self):
        return self.title + ' by ' + self.author.username
