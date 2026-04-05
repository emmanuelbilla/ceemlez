from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    '''
    Serializer for the CustomUser model. It includes fields for user details and specifies read-only fields. The Meta class defines the model and fields to be serialized.
    '''
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'organisation',
        ]
        read_only_fields = ['id', 'is_staff', 'is_active', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    '''
    Serializer for user registration.
    password is write-only and must be at least 8 characters long.
    Meta class specifies the model and fields to be serialized. The create method is overridden to handle user creation with password hashing.
    '''
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'organisation', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        return CustomUser.objects.create_user(password=password, **validated_data)


class LoginSerializer(serializers.Serializer):
    '''
    Serializer for user login. It includes fields for email and password, where password is write-only. This serializer is used to validate login credentials.
    '''
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
