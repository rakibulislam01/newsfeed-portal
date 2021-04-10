from django.db import models
from user.models import User


class EmailNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    send_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
