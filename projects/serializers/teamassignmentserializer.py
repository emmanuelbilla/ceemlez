from rest_framework import serializers
from projects.models.teamassignment import TeamAssignment


# Serializer for TeamAssignment model
class TeamAssignmentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # Automatically set the owner to the logged-in user

    class Meta:
        model = TeamAssignment
        fields = '__all__'  # Include all fields of the model
    
def validate(self, data):
    if TeamAssignment.objects.filter(
        user=data['user'],
        task=data['task']
    ).exists():
        raise serializers.ValidationError("This user is already assigned to this task.")
    return data