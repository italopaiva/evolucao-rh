from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='admin_home'),
    url(r'budget$', views.budgets, name='admin_budget'),
]