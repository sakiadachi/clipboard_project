from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from clipboard.models import Clipboard
from clipboard.serializers import ClipboardSerializer


class ClipboardViewSet(viewsets.ModelViewSet):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]