from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    """Model for product"""
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Product Name',
    )
    description = models.TextField(
        verbose_name='Product description',
    )
    price = models.PositiveIntegerField(
        #  The Checkout Session's total amount must convert to
        #  at least 50 cents with taxes.
        validators=[MinValueValidator(100), ],
        verbose_name='Product price in cents',
    )

    def __str__(self) -> str:
        return self.name
