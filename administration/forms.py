#coding=utf-8
from django import forms
from .models import Company, StartPage

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class StartPageForm(forms.ModelForm):
    class Meta:
        model = StartPage
        fields = '__all__'
        widgets = {
            'pic1': forms.FileInput(attrs={
                'class': 'filestyle',
                'data-buttonText': 'Selecionar foto',
                'data-placeholder': 'Nenhuma foto selecionada',
            }),
            'pic2': forms.FileInput(attrs={
                'class': 'filestyle',
                'data-buttonText': 'Selecionar foto',
                'data-placeholder': 'Nenhuma foto selecionada',
            }),
            'pic3': forms.FileInput(attrs={
                'class': 'filestyle',
                'data-buttonText': 'Selecionar foto',
                'data-placeholder': 'Nenhuma foto selecionada',
            })
        }