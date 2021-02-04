from django import forms
from testapp.models import Studentregister

class StudentForm(forms.ModelForm):
    class Meta:
        model=Studentregister
        fields="__all__"
