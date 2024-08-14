from django.shortcuts import render
from .models import Project


def projects(requests):
    pr = Project.objects.all()
    context = {'projects': pr}
    return render(requests, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project': project_obj}
    return render(request, "projects/single-project.html", context)
