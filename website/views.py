# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib import messages
from website.models import Service, Budget, BudgetService
from website.forms import NewBudgetForm, EmployeeBudgetForm

def home(request):
    return TemplateResponse(request, "home.html")

def services(request):
    available_services = Service.objects.all()
    context = {
        'services': available_services
    }
    return TemplateResponse(request, "services.html", context)

def we(request):
    return TemplateResponse(request, "we.html")

def budget(request):
    available_services = Service.objects.all()
    context = {
        'services': available_services,
        'form': NewBudgetForm(),
        'service_form': EmployeeBudgetForm(),
    }
    return TemplateResponse(request, "budget.html", context)

def join_us(request):
    return TemplateResponse(request, "join_us.html")

def contact(request):
    return TemplateResponse(request, "contact.html")

class NewBudgetView(View):
    def post(self, request):
        data = request.POST
        budget_form = NewBudgetForm(data=data)
        employees_form = EmployeeBudgetForm(data=data)
        if(budget_form.is_valid()):
            budget = self.save_budget(data)
            self.save_budget_employees(budget, data)

            msg_level = messages.SUCCESS
            msg = u'Orçamento solicitado com sucesso, %s!' % data['requester']
            messages.add_message(request, msg_level, msg)

            response = HttpResponseRedirect(reverse('budget'))
        else:
            available_services = Service.objects.all()
            context = {
                'services': available_services,
                'form': budget_form,
                'service_form': employees_form,
            }
            response = TemplateResponse(request, "budget.html", context)
        return response

    def save_budget(self, data):
        budget = Budget.objects.create(
            requester=data['requester'],
            requester_email=data['requester_email'],
            requester_phone=data['requester_phone'],
            requester_address=data['requester_address'],
            message=data['message']
        )
        return budget

    def save_budget_employees(self, budget, data):
        for service, service_id in Service.SERVICES:
            if data[service] != 'None':
                BudgetService.objects.create(
                    budget=budget,
                    service=Service.objects.get(pk=service_id),
                    quantity=data[service]
                )

