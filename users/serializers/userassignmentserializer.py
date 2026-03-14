from rest_framework import serializers
from users.models.userassignment import UserAssignment


# Serializer for UserAssignment model
class UserAssignmentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # Automatically set the owner to the logged-in user

    class Meta:
        model = UserAssignment
        fields = '__all__'  # Include all fields of the model
    
def validate(self, data):
    if UserAssignment.objects.filter(
        user=data['user'],
        task=data['task']
    ).exists():
        raise serializers.ValidationError("This user is already assigned to this task.")
    return data