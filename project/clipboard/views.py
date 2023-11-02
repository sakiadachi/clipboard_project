from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from clipboard.models import Clipboard
from clipboard.serializers import ClipboardSerializer


class ClipboardViewSet(viewsets.ModelViewSet):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]