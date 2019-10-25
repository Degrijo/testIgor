from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from core.forms import TaskForm
from core.models import Task


class TaskListFormView(FormView):
    template_name = 'core/main_page.html'
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['tasks'] = Task.objects.all().order_by('status')
        return context


class TaskDetailFormView(FormView):
    template_name = 'core/task_page.html'
    form_class = TaskForm

    # def dispatch(self, request, *args, **kwargs):
    #     try:
    #         Task.objects.get(id=request.GET.get('pk'))
    #     except ObjectDoesNotExist:
    #         return reverse('task_list_form_view')
    #     finally:
    #         return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.get(id=self.kwargs['pk'])
        context['rezult'] = 'your query'
        return context
