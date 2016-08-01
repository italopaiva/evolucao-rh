from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='admin_home'),
    url(r'budget$', views.budgets, name='admin_budget'),
    url(r'budget_answered/(?P<budget_id>[0-9]+)$', views.answered_budgets, name='budget_answered'),
]