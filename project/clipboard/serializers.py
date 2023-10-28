from rest_framework import serializers
from clipboard.models import Clipboard
from django.contrib.auth.models import User

class ClipboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clipboard
        fields = ['id', 'title', 'text',]
