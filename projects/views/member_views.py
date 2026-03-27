from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from projects.models.team_member import TeamMember
from projects.serializers.teammemberserializer import TeamMemberSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from core.permissions import IsOwnerOrReadOnly


# List and Create Projects
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update, and Delete a Project
class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    #permission_classes = [IsOwnerOrReadOnly] # Allows only owners to edit or delete