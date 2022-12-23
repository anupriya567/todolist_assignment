from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

task_router = DefaultRouter()
task_router.register('',views.TaskVS,basename="task")

urlpatterns = [
    path('tasks/', include(task_router.urls)),
    path('task/<pk>/mark', views.ToogleCompletion.as_view(), name = "toggle-completion")
    
    # path(task/<id:pk>, views.TaskDetail, name = "task-detail"),  

]
