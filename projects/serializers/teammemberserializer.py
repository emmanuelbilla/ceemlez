from rest_framework import serializers
from projects.models.team_member import TeamMember


# Serializer for TeamMember model
class TeamMemberSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # Automatically set the owner to the logged-in user

    class Meta:
        model = TeamMember
        fields = '__all__'  # Include all fields of the model
    
def validate(self, data):
    if TeamMember.objects.filter(
        user=data['user'],
        task=data['project']
    ).exists():
        raise serializers.ValidationError("This user is already added to this project.")
    return data