#coding=utf-8
from django import forms
from website.models import Budget, BudgetService

class NewBudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
        exclude = ['answered']

def get_choices():
    choices = []
    choices.append(('None', 'Não preciso'))
    for i in range(1,11):
        choices.append((i, i))
    choices.append(('11', 'Mais de 10'))
    return choices


class EmployeeBudgetForm(forms.Form):
    doorman = forms.ChoiceField(label="Porteiro", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    recepcionist = forms.ChoiceField(label="Recepcionista", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    brigadist = forms.ChoiceField(label="Brigadista", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    cleaner = forms.ChoiceField(label="Agente de Limpeza", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    janitor = forms.ChoiceField(label="Zelador", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    cupbearer = forms.ChoiceField(label="Copeiro", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    maid = forms.ChoiceField(label="Camareira", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    gardener = forms.ChoiceField(label="Jardineiro", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    pool_guy = forms.ChoiceField(label="Piscineiro", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    driver = forms.ChoiceField(label="Motorista", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    motoboy = forms.ChoiceField(label="Motoboy", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    parker = forms.ChoiceField(label="Garagista", choices=get_choices(), widget=forms.Select(attrs={'class':'form-control'}))