from rest_framework import serializers
from users.models.new_user import NewUser

# Serializer for NewUser model
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'