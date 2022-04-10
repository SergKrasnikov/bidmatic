from datetime import date
from django import forms
from django.forms.utils import ErrorList

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
        if bidding == 'None':
            # It is necessary to completely nullify the errors that could come to us
            # after calling the method of the inherited class
            errors = self.errors.setdefault('bidding', ErrorList())
            # Now add your error
            errors.append('This field is required.')

        # exercise: Any other validation you think is required.
        # Lack of understanding of the objectives of this data collection
        # does not make it clear what additional checks need to be carried out

        return self.cleaned_data

    @staticmethod
    def age(birthday: int) -> int:
        today = date.today()

        if today.month < birthday.month or\
                (today.month == birthday.month and today.day < birthday.day):
            return today.year - birthday.year - 1
        else:
            return today.year - birthday.year

    class Meta:
        model = Account
        fields = '__all__'
