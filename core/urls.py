from django.urls import path
from core.views import TaskListFormView, TaskDetailFormView


urlpatterns = [
    path('', TaskListFormView.as_view(), name='task_list_form_view'),
    path('task-<int:pk>', TaskDetailFormView.as_view(), name='task_detail_form_view'),
]
