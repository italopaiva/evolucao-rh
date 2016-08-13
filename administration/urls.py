from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='admin_home'),
    url(r'budget$', views.budgets, name='admin_budget'),
    url(r'resumes$', views.resume_requests, name='admin_resumes'),
    url(r'answered_budgets$', views.answered_budgets, name='answered_budgets'),
    url(r'answered_resume$', views.answered_resume, name='answered_resume'),
    url(r'resume_answered/(?P<resume_id>[0-9]+)$', views.answer_resume, name='resume_answered'),
    url(r'budget_answered/(?P<budget_id>[0-9]+)$', views.answer_budget, name='budget_answered'),
    url(r'update_company_data$', views.update_company, name='update_company_data'),
    url(r'start_page$', views.StartPageView.as_view(), name='admin_start_page'),
]