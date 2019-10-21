from django.contrib.auth.models import Group
from rest_framework import viewsets
from django_user_management.apps.user_management.serializers import UserSerializer, GroupSerializer
from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from guardian.shortcuts import assign_perm

from .permissions import IsCreatedByOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, IsCreatedByOrReadOnly]

    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
