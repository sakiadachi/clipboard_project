from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from clipboard.models import Clipboard
from clipboard.serializers import ClipboardSerializer, RegisterUserSerializer
from django.contrib.auth.models import User
from clipboard.serializers import UserSerializer


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

class RegisterUserView(generics.CreateAPIView) :
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer