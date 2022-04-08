# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth.views import LoginView

__author__ = 'AlexStarov'

urlpatterns = [
    path('', LoginView.as_view(
                template_name='auth.html',
                redirect_authenticated_user=True),
         name='authentication'),
]
