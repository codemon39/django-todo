from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.tasks, name="tasks"),
    path("deltasks/<int:id>", views.deltasks, name="deltasks"),
    path("updtasks/<int:id>", views.updtasks, name="updtasks"),
    path(
        "base/tasks/doupdtask/<int:id>/", views.doupdate, name="doupdtasks"
    ),  # For processing the form
]
