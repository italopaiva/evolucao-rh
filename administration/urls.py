from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='admin_home'),
    url(r'budget$', views.budgets, name='admin_budget'),
    url(r'resumes$', views.resume_requests, name='admin_resumes'),
    url(r'resume_answered/(?P<resume_id>[0-9]+)$', views.answer_resume, name='resume_answered'),
    url(r'budget_answered/(?P<budget_id>[0-9]+)$', views.answered_budgets, name='budget_answered'),
]