from .models import StudentModel
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'