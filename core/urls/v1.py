from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet
from newsletters.views import NewsletterViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'newsletters', NewsletterViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
