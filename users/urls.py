from django.urls import path
from users.views.users_views import NewUserListCreateView, NewUserDetailView


app_name = 'users'

urlpatterns = [
    path('', NewUserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', NewUserDetailView.as_view(), name='user-detail'),
]