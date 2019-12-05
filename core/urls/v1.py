from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet
from newsletters.views import NewsletterViewSet
from tags.views import TagsViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'newsletters', NewsletterViewSet)
routers.register(r'tags', TagsViewSet)


urlpatterns = [
    path('', include(routers.urls))
]
