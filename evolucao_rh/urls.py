"""evolucao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from website import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^login$', auth_views.login, {'template_name': 'login.html'}, "login"),
    url(r'^logout$', auth_views.logout, {'next_page': 'home'}, "logout"),
    url(r'^administration/', include('administration.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^services$', views.services, name='services'),
    url(r'^we$', views.we, name='us_who'),
    url(r'^budget$', views.budget, name='budget'),
    url(r'^join_us$', views.join_us, name='join_us'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^new_budget$', views.NewBudgetView.as_view(), name='new_budget'),
]