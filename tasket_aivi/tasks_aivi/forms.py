from django import forms
from . import models


class TaskForm(forms.ModelForm):
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = models.Task
        fields = ('name', 'project', 'description', 'deadline', 'is_done' )