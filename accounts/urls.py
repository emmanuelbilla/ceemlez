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
