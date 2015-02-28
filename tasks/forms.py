from django import forms
from models import Task
from models import Relax

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'category', 'task_photo', )

class CreatePrikolForm(forms.ModelForm):
    class Meta:
        model = Relax
        fields = ('title', 'description', 'category', 'relax_foto', )
