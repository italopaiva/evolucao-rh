# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import View
from website.models import Budget, BudgetService, Service, JoinUsRequest
from .models import Company, StartPage
from .forms import CompanyForm, StartPageForm

@login_required
def home(request):
    try:
        # Try to find previous company data on database
        company = Company.load()
        form = CompanyForm(instance=company)
    except Company.DoesNotExist:
        # If previous data not exists, return an empty form
        form = CompanyForm()
    context = {'form': form}
    return TemplateResponse(request, 'admin_home.html', context)

@login_required
def update_company(request):
    try:
        company = Company.load()
        form = CompanyForm(instance=company, data=request.POST)
    except Company.DoesNotExist:
        form = CompanyForm(data=request.POST)

    if form.is_valid():
        form.save()
        msg_level = messages.SUCCESS
        msg = u'Dados atualizados com sucesso!'
        response = HttpResponseRedirect(reverse('admin_home'))
    else:
        context = {'form': form}
        msg_level = messages.ERROR
        msg = u'Não foi possível atualizar os dados. Cheque os dados informados.'
        response = TemplateResponse(request, 'admin_home.html', context)
    messages.add_message(request, msg_level, msg)
    return response

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
def answer_budget(request, budget_id):
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

@login_required
def answer_resume(request, resume_id):
    resume = JoinUsRequest.objects.get(pk=resume_id)
    resume.answered = True
    resume.save()
    msg_level = messages.SUCCESS
    msg = u'Currículo marcado como respondido com sucesso!'
    messages.add_message(request, msg_level, msg)
    return HttpResponseRedirect(reverse('admin_resumes'))

@login_required
def answered_budgets(request):
    budgets = BudgetService.objects.filter(budget__answered=True).order_by('-budget__date')
    budgets = group_by_budget(budgets)
    context = {'budgets': budgets.items()}
    return TemplateResponse(request, 'answered_budgets.html', context)

@login_required
def answered_resume(request):
    resumes = JoinUsRequest.objects.filter(answered=True).order_by('-date')
    context = {'resumes': resumes}
    return TemplateResponse(request, 'answered_resumes.html', context)


class StartPageView(View):

    @method_decorator(login_required)
    def get(self, request):
        try:
            start_page = StartPage.load()
            form = StartPageForm(instance=start_page)
        except StartPage.DoesNotExist:
            form = StartPageForm()
        context = {'form': form}
        print
        print(context['form'])
        return TemplateResponse(request, 'configure_start_page.html', context)

    @method_decorator(login_required)
    def post(self, request):
        try:
            start_page = StartPage.load()
            form = StartPageForm(request.POST, request.FILES, instance=start_page)
        except StartPage.DoesNotExist:
            form = StartPageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            msg_level = messages.SUCCESS
            msg = u'Dados atualizados com sucesso!'
            response = HttpResponseRedirect(reverse('admin_start_page'))
        else:
            context = {'form': form}
            msg_level = messages.ERROR
            msg = u'Não foi possível atualizar os dados. Cheque os dados informados.'
            response = TemplateResponse(request, 'configure_start_page.html', context)
        messages.add_message(request, msg_level, msg)
        return response