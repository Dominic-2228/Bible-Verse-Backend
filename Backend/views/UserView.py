from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model
from Backend.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from django.contrib.auth import authenticate

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
    permission_classes = [permissions.AllowAny, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Optionally, set the user to the currently logged-in user
        # For normal User creation by registration, you might handle this differently
        serializer.save()

    def profile(self, request):
        """Return data for the currently authenticated user"""
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer
        Purpose: Allow a user to communicate with the Bangazon database to retrieve  one user
        Methods:  GET
        Returns:
            Response -- JSON serialized customer instance
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={"request": request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to user resource"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=False, methods=["post"], url_path="register")
    def register_account(self, request):
        serializer = UserSerializer(data=request.data)
        is_superuser = request.data.get("is_superuser", False)
        if serializer.is_valid():
            if is_superuser:
                # This sets is_staff=True and is_superuser=True automatically
                user = User.objects.create_superuser(
                    username=serializer.validated_data["username"],
                    password=serializer.validated_data["password"],
                    first_name=serializer.validated_data["first_name"],
                    last_name=serializer.validated_data["last_name"],
                    email=serializer.validated_data["email"],
                )
            else:
                user = User.objects.create_user(
                    username=serializer.initial_data["username"],
                    password=serializer.initial_data["password"],
                    first_name=serializer.initial_data["firstname"],
                    last_name=serializer.initial_data["lastname"],
                    email=serializer.initial_data["email"],
                )

            if serializer.validated_data.get("is_superuser", False):
                user.is_superuser = True
                user.is_staff = True   # usually needed so they can access Django admin
                user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"id": user.id, "username": user.username, "is_staff": user.is_staff, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["post"], url_path="login")
    def user_login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            serialized_user = UserSerializer(user)
            return Response({"user": serialized_user.data, "token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                []
            )
