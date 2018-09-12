from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4


# Create your models here.
User = get_user_model()


def deserialize_user(user):
    """Deserialize user instance to JSON"""
    return {
        'id': user.id, 'username': user.username, 'email': user.email,
        'first_name': user.first_name, 'last_name': user.last_name
    }


def _generate_unique_uri():
    """Generate a unique uri for the chat session"""
    return str(uuid4()).replace('-', '')[:15]


class TrackableDateModel(models.Model):
    """Abstract model to track the creation/updated date for a model"""

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChatSession(TrackableDateModel):
    """Model to store chat session"""
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    uri = models.URLField(default=_generate_unique_uri)


class ChatSessionMessage(TrackableDateModel):
    """Model to store chat message"""
    message = models.TextField()
    chat_session = models.ForeignKey(ChatSession,
                                     related_name='messages',
                                     on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def to_json(self):
        """deserialize message to JSON"""
        return {'user': deserialize_user(self.user), 'message': self.message}


class ChatSessionMember(TrackableDateModel):
    """Model to store chat user"""
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    chat_session = models.ForeignKey(ChatSession,
                                     related_name='members',
                                     on_delete=models.PROTECT)
