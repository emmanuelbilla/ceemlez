from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views.users_views import UserListCreateView, UserDetailView
from users.views.userassignment_views import UserAssignmentViewSet


app_name = 'users'
router = DefaultRouter()
router.register(r'assignments', UserAssignmentViewSet, basename='assignments')

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

] + router.urls