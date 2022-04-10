from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Account
from .forms import AccountForm


@login_required
class AccountListView(ListView):

    model = Account
    template_name = 'list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
class AccountCreateView(CreateView):
    model = Account
    template_name = 'add.html'
    form_class = AccountForm
    success_url = '/accounts/list/'


@login_required
class AccountRemoveView(DeleteView):
    model = Account
    success_url = '/accounts/list/'
