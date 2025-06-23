from django.urls import path
from mytodo import views  

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("update_task_complete/", views.update_task_complete, name="update_task_complete"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
