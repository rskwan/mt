from django.db import models
from djmoney.models.fields import MoneyField

class Payable(models.Model):
    fee = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='USD'
    )

    class Meta:
        abstract = True

class Permalinkable(models.Model):
    slug = models.SlugField(
        unique=True,
        help_text=("A short, unique string that will "
                   "represent this object in URLs.")
    )

    class Meta:
        abstract = True
