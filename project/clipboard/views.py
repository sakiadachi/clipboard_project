from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from clipboard.models import Clipboard
from clipboard.serializers import ClipboardSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from clipboard.serializers import UserSerializer
from rest_framework.response import Response


class ClipboardViewSet(viewsets.ModelViewSet):
    queryset = Clipboard.objects.all()
    serializer_class = ClipboardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Clipboard.objects.filter(created_by=user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer