import uuid

from django.db import models

class Article (models.Model):
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField (max_length=256)
    author = models.CharField (max_length=256)
    body_text = models.TextField()

    def __str__(self) -> str:
        return self.title
