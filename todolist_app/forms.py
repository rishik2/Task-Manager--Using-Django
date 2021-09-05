from django import forms
from todolist_app.models import TaskList

#creating forms class that will take models class and fields
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']
