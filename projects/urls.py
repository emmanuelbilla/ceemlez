from .views.task_views import TaskListCreateView, TaskDetailView
from .views.project_views import ProjectListCreateView, ProjectDetailView
from .views.member_views import MemberListCreateView, MemberDetailView
from .views.assignment_views import AssignmentListCreateView, AssignmentDetailView
from django.urls import path


urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('members/', MemberListCreateView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('assignments/', AssignmentListCreateView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),

]
