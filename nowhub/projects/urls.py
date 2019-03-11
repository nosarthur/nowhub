from django.urls import path, include
from rest_framework import routers

from projects import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
