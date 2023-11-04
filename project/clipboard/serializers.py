from rest_framework import serializers
from clipboard.models import Clipboard
from django.contrib.auth.models import User

class ClipboardSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')

    class Meta:
        model = Clipboard
        fields = ['id', 'title', 'text', 'created_date', 'created_by', 'updated_by']


class UserSerializer(serializers.ModelSerializer):
    clipboards = serializers.PrimaryKeyRelatedField(many=True, queryset=Clipboard.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'clipboards']