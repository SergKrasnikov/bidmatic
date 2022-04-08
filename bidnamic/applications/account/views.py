from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Account
from .forms import AccountForm


class AccountListView(ListView):

    model = Account
    template_name = 'list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AccountCreateView(CreateView):
    model = Account
    template_name = 'add.html'
    form_class = AccountForm
    success_url = '/accounts/list/'
