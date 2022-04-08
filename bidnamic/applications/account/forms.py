from django import forms
from django.forms.utils import ErrorList
from datetime import datetime, date

from .models import Account


class AccountForm(forms.ModelForm):

    bidding = forms.CharField(
        required=True,
        widget=forms.Select(choices=Account.BIDDING_VAR),
    )

    def clean(self):
        super().clean()

        birthday = self.cleaned_data.get('birthday')

        if self.age(birthday=birthday) < 18:
            self.add_error('birthday', 'Unfortunately access is denied due to age restrictions.')

        bidding = self.cleaned_data.get('bidding')
        print(self.cleaned_data)
        print(bidding)
        print(type(bidding))
        if bidding is None:
            errors = self._errors.setdefault('binding', ErrorList())
            errors.append('This field is required.')

        return self.cleaned_data

    @staticmethod
    def age(birthday):
        today = date.today()

        if today.month < birthday.month or\
                (today.month == birthday.month and today.day < birthday.day):
            return today.year - birthday.year - 1
        else:
            return today.year - birthday.year

    class Meta:
        model = Account
        fields = '__all__'
