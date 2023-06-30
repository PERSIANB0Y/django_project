from django import forms
from main2.models import Student


class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "pic"]
