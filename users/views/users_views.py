from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from users.models.new_user import User
from users.serializers.usersserializer import UserSerializer


# List and Create Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve, Update, and Delete a User
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer