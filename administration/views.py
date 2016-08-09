# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from website.models import Budget, BudgetService, Service, JoinUsRequest

@login_required
def home(request):
    return TemplateResponse(request, 'admin_home.html')

def group_by_budget(budget_services):
    grouped_budgets = {}
    for budget_service in budget_services:
        budget_id = budget_service.budget
        if budget_id in grouped_budgets:
            grouped_budgets[budget_id].append(budget_service)
        else:
            grouped_budgets[budget_id] = []
    return grouped_budgets

@login_required
def budgets(request):
    budgets = BudgetService.objects.filter(budget__answered=False).order_by('-budget__date')
    budgets = group_by_budget(budgets)
    context = {'budgets': budgets.items()}
    return TemplateResponse(request, 'admin_budget.html', context)

@login_required
def answered_budgets(request, budget_id):
    budget = Budget.objects.get(pk=budget_id)
    budget.answered = True
    budget.save()
    msg_level = messages.SUCCESS
    msg = u'Orçamento marcado como respondido com sucesso!'
    messages.add_message(request, msg_level, msg)
    return HttpResponseRedirect(reverse('admin_budget'))

@login_required
def resume_requests(request):
    resumes = JoinUsRequest.objects.filter(answered=False).order_by('-date')
    context = {'resumes': resumes}
    return TemplateResponse(request, 'admin_resumes.html', context)

def answer_resume(request, resume_id):
    resume = JoinUsRequest.objects.get(pk=resume_id)
    resume.answered = True
    resume.save()
    msg_level = messages.SUCCESS
    msg = u'Currículo marcado como respondido com sucesso!'
    messages.add_message(request, msg_level, msg)
    return HttpResponseRedirect(reverse('admin_resumes'))
