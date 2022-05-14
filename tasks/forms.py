# import form class from django
from django import forms

from .models import Tasks
  
# create a ModelForm
class TasksForm(forms.ModelForm):
    # specify the name of model to use
    # specifying the fields to appear on the form
    class Meta:
        model = Tasks
        fields = "__all__"