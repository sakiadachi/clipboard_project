import uuid

from django.db import models

class Clipboard(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='updated_by', blank=True, null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_date']