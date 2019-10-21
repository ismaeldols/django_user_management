from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        User = get_user_model()
        model = User
        fields = ['url', 'username', 'email', 'iban', 'groups', 'created_by']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
