
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            'title',
            'description',
            'due_date',
            'priority',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter task description',
                'rows': 4,
                'class': 'form-control',
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
