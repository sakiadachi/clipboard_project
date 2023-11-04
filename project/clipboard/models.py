import uuid

from django.db import models

class Clipboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.CharField(max_length=100, blank=True, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, related_name='updated_by', blank=True, null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'clipboard'
        ordering = ['created_date']