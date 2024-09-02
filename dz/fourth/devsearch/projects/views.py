from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(requests):
    pr = Project.objects.all()
    context = {'projects': pr}
    return render(requests, "projects/projects.html", context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {'project': project_obj}
    return render(request, "projects/single-project.html", context)


def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/form-template.html', context)
