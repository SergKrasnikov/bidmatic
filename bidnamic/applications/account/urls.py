# -*- coding: utf-8 -*-

from django.urls import path
from .views import AccountListView, AccountCreateView

__author__ = 'AlexStarov'

urlpatterns = [
    path('list/', AccountListView.as_view(), name='accounts_list'),
    path('add/', AccountCreateView.as_view(), name='accounts_add'),
]
