from django.shortcuts import render

from rest_framework import viewsets

from projects.models import Project
from projects.serializers import ProjectSerializer


def homepage(request):
    projs = Project.objects.all()
    context = {'projects': projs}
    return render(request, 'index.html', context)



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
