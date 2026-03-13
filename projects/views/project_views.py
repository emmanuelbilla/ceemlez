from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from projects.models.project import Project
from projects.serializers.projectserializer import ProjectSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from core.permissions import IsOwnerOrReadOnly


# List and Create Projects
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update, and Delete a Project
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class =ProjectSerializer
    #permission_classes = [IsOwnerOrReadOnly] # Allows only owners to edit or delete