from django import forms
from website.models import Budget

class NewBudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = '__all__'