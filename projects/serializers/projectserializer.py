from rest_framework import serializers
from projects.models.project import Project

# Serializer for Project model
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'