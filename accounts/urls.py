from django.urls import include, path
from rest_framework.routers import DefaultRouter

from accounts.views import AccountViewSet
'''
Using a router to automatically determine the URL conf for our API.
The API URLs are now determined automatically by the router.
Additionally, we include login URLs for the browsable API.
'''
router = DefaultRouter()
router.register('users', AccountViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
]
'''
Adds up endpoints for urls including:
users/$ [name='accounts-list'] - for listing and creating accounts
^users\.(?P<format>[a-z0-9]+)/?$ [name='accounts-list'] - for listing and creating accounts with format suffix
^users/login/$ [name='accounts-login'] - for logging in users
^users/login\.(?P<format>[a-z0-9]+)/?$ [name='accounts-login'] - for logging in users with format suffix
^users/logout/$ [name='accounts-logout'] - for logging out users
^users/logout\.(?P<format>[a-z0-9]+)/?$ [name='accounts-logout'] - for logging out users with format suffix
^users/(?P<pk>[^/.]+)/$ [name='accounts-detail'] - for retrieving, updating, or deleting a specific account
^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='accounts-detail'] - for retrieving, updating, or deleting a specific account with format suffix
[name='api-root'] 
'''