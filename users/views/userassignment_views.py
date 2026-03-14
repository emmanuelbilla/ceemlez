from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from users.models.userassignment import UserAssignment
from users.serializers.userassignmentserializer import UserAssignmentSerializer
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from .permissions import IsProjectOwnerOrReadOnly

# ViewSet for UserAssignment
class UserAssignmentViewSet(ModelViewSet):
    queryset = UserAssignment.objects.all()
    serializer_class = UserAssignmentSerializer
    #permission_classes = [IsProjectOwnerOrReadOnly] # Custom permission class