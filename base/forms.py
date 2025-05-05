from django import forms
from .models import Task
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'tag']