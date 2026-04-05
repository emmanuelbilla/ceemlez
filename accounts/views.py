from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, RegisterSerializer, LoginSerializer


class AccountViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    '''
    ViewSet for managing user accounts.
    It includes actions for listing, retrieving, creating users, and custom actions for login and logout. Permissions are set based on the action being performed.
    '''
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # Override get_serializer_class to return RegisterSerializer for the create action, and the default serializer for other actions.
    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        return super().get_serializer_class()

    # Override get_permissions to set permissions based on the action. AllowAny for create and login, IsAuthenticated for logout and other actions.
    def get_permissions(self):
        if self.action in ('create', 'login'):
            permission_classes = [AllowAny]
        elif self.action == 'logout':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    # Override create method to handle user registration. It validates the input data, creates a new user, and returns the user data in the response.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = CustomUserSerializer(user).data
        return Response(user_data, status=status.HTTP_201_CREATED)

    # Custom action for user login. It validates the login credentials, authenticates the user, and returns the user data if successful. If authentication fails, it returns an error response. 
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )
        if not user:
            return Response(
                {'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED
            )

        auth_login(request, user)
        user_data = CustomUserSerializer(user).data
        return Response(user_data, status=status.HTTP_200_OK)

    # Custom action for user logout. It logs out the authenticated user and returns a success message in the response.
    @action(detail=False, methods=['post'])
    def logout(self, request):
        auth_logout(request)
        return Response(
            {'detail': 'User successfully logged out'}, status=status.HTTP_200_OK
        )
