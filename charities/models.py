from django.db import models
from django import forms

class Charity(models.Model):
    charity_name = models.CharField(max_length=200)
    charity_description = models.CharField(max_length=200)
    ripple_id = models.CharField(max_length=200)

class Request(models.Model):
	address = models.CharField(max_length=200)
	amount = models.DecimalField(max_length=200, decimal_places=9, max_digits=15)
	date = models.DateTimeField(auto_now=True)
	is_transaction_complete = models.BooleanField(default=False)
	is_valid = models.BooleanField(default=True)

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request