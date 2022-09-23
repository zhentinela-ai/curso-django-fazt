from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from myapp.forms import CreateNewProject, CreateNewTask
from .models import Project, Task


# Create your views here.
def index(request):
    title = "Welcome to Django Course!!!"
    return render(request, 'index.html', {'title': title})


def about(request):
    username = "zhent"
    return render(request, 'about.html', {'username': username})


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/project.html', {'projects': projects})


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


def create_task(request):

    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html',
                      {'form': CreateNewTask()})
    else:
        Task.objects.create(title=request.POST["title"],
                            description=request.POST["description"],
                            project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',
                      {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })