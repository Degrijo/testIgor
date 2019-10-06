from .models import Task
from django.forms import forms


class TaskForm(forms.Form):
    class Meta:
        model = Task
        exclude = 'done'
