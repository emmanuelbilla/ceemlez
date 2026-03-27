from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from projects.models.teamassignment import TeamAssignment
from projects.serializers.teamassignmentserializer import TeamAssignmentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from core.permissions import IsOwnerOrReadOnly


# List and Create Projects
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = TeamAssignment.objects.all()
    serializer_class = TeamAssignmentSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update, and Delete a Project
class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamAssignment.objects.all()
    serializer_class = TeamAssignmentSerializer
    #permission_classes = [IsOwnerOrReadOnly] # Allows only owners to edit or delete