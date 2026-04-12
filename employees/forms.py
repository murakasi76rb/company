from django import forms
from employees.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email']


    def clean_email(self):
        BLOCKED_DOMEN: list[str] = ['yandex.ru', 'ya.ru',]
        email:str = self.cleaned_data['email']
        domain: str = email.split('@')[-1]
        if domain in BLOCKED_DOMEN:
            raise forms.ValidationError("This domen email blocked")
        return email


EmployeeFormSet = forms.modelformset_factory(Employee, fields=("name", "email"), extra=3)