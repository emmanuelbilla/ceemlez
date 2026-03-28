from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from users.models.new_user import NewUser
from users.serializers.usersserializer import NewUserSerializer


# List and Create Users
class NewUserListCreateView(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer

# Retrieve, Update, and Delete a User
class NewUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer