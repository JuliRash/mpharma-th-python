import uuid
from django.db import models
from django.utils import timezone


class Diagnosis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_code = models.CharField(max_length=255, blank=True)
    category_title = models.CharField(max_length=255, blank=True)
    diagnosis_code = models.CharField(max_length=255, blank=True)
    full_code = models.CharField(max_length=255, blank=True)
    abbreviated_description = models.CharField(max_length=255, blank=True)
    full_description = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.category_title
