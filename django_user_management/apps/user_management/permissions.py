from rest_framework import permissions


class IsCreatedByOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow creators of an object to edit it.
    Assumes the model instance has an 'created_by' attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # So we'll always allos GET, HEAD or OPTIONS request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named 'created_by'
        return obj.created_by == request.user
