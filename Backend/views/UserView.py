from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from Backend.serializers import UserSerializer

User = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only the user themselves can edit or delete their account.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the account
        return obj == request.user


class UserView(viewsets.ModelViewSet):
    """
    Full CRUD for User, but only allows the logged-in user to update/delete themselves.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Optionally, set the user to the currently logged-in user
        # For normal User creation by registration, you might handle this differently
        serializer.save()
