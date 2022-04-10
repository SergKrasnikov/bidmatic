from django.test import TestCase

from http import HTTPStatus


class AccountFormTest(TestCase):

    def test_accounts_add_REDIRECT(self):
        response = self.client.post("/accounts/add/", data={
            "title": "Ser", "first_name": "Alex", "surname": "Astarov", "birthday": "01/06/1978",
            "company_name": "Bidnamic", "address": "str.", "telephone": "+40 78 123-345",
            "bidding": "M", "google_ads_acc_id": "12345678"})

        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_accounts_add_Error_age_restrictions(self):

        response = self.client.post("/accounts/add/", data={
            "title": "Ser", "first_name": "Serhii", "surname": "Krasnikov", "birthday": "01/06/2010",
            "company_name": "Bidnamic", "address": "str.", "telephone": "+40 78 123-345",
            "bidding": "L", "google_ads_acc_id": "12345678"})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Unfortunately access is denied due to age restrictions.", html=True)

    def test_accounts_add_Error_not_selected_field_bidding(self):

        response = self.client.post("/accounts/add/", data={
            "title": "Ser", "first_name": "Alex", "surname": "Starov", "birthday": "01/01/2001",
            "company_name": "Bidnamic", "address": "str.", "telephone": "+40 78 123-345",
            "bidding": "None", "google_ads_acc_id": "12345678"})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "This field is required.", html=True)
