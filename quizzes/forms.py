from django import forms
from .models import Answer

class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
