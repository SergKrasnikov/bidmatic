from datetime import datetime
from django.db import models


class Account(models.Model):
    """ Account List """

    title = models.CharField(verbose_name="Title", max_length=8, blank=True)
    first_name = models.CharField(verbose_name="First name", max_length=32, blank=True)
    surname = models.CharField(verbose_name="Surname", max_length=32, blank=True)
    birthday = models.DateField(verbose_name='Date of Birth', blank=False, default=datetime.today)
    company_name = models.CharField(verbose_name='Company Name', max_length=64, blank=True)
    address = models.CharField(verbose_name='Address', max_length=128, blank=True)
    telephone = models.CharField(verbose_name='Telephone', max_length=16, blank=True)

    BIDDING_VAR = (
        ('H', 'HIGH'),
        ('M', 'MEDIUM'),
        ('L', 'LOW'),
    )
    # default 'N' value means None
    bidding = models.CharField(verbose_name='Bidding Settings(choose one)',
                               max_length=1, choices=BIDDING_VAR, blank=False, default='N')
    google_ads_acc_id = models.CharField(verbose_name='Google Ads Account ID', max_length=16, blank=True)
