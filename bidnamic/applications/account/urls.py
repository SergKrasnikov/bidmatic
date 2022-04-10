# -*- coding: utf-8 -*-

from django.urls import path
from .views import AccountListView, AccountCreateView, AccountRemoveView

__author__ = 'AlexStarov'

app_name = 'account'

urlpatterns = [
    path('list/', AccountListView.as_view(), name='list'),
    path('add/', AccountCreateView.as_view(), name='add'),
    path('remove/<int:pk>/', AccountRemoveView.as_view(), name='remove'),
]
