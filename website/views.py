from django.shortcuts import render
from django.template.response import TemplateResponse
from website.models import Service

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
        'services': available_services
    }
    return TemplateResponse(request, "budget.html", context)

def join_us(request):
    return TemplateResponse(request, "join_us.html")

def contact(request):
    return TemplateResponse(request, "contact.html")
