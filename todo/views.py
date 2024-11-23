from django.shortcuts import render, redirect
from todo.models import *


# Create your views here.
def home(request):
    success = False
    if request.method == "POST":

        title = request.POST.get("title")
        desc = request.POST.get("desc")

        ins = Tasks(title=title, description=desc)
        ins.save()
        success = True
    return render(request, "home.html", {"success": success})


def tasks(request):
    my_tasks = Tasks.objects.all()
    context = {"tasks": my_tasks}
    return render(request, "tasks.html", context)


def deltasks(request, id):
    del_task = Tasks.objects.get(id=id)
    del_task.delete()
    return redirect("tasks")


def updtasks(request, id):
    task = Tasks.objects.get(id=id)

    if request.method == "POST":
        return redirect("doupdtasks", id=id)  # Redirect to form processing view

    return render(request, "update.html", {"task": task})


def doupdate(request, id):
    task = Tasks.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        task.title = title
        task.description = desc
        task.save()

        return redirect("tasks")

    return render(request, "update.html", {"task": task})
