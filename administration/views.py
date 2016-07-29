from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return TemplateResponse(request, 'admin_home.html')

@login_required
def budgets(request):
    return TemplateResponse(request, 'admin_budget.html')