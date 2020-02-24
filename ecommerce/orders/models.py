from decimal import Decimal
from django.db import models
from carts.models import Cart
# from django.contrib.auth import get_user_model
from django.conf import settings
from accounts.models import UserAddress
# User = get_user_model()

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120, default='ABC', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
    # user
    # address
    shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address', on_delete=models.CASCADE, default=1)
    billing_address = models.ForeignKey(UserAddress, related_name='billing_address', on_delete=models.CASCADE, default=1)
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

    def get_final_amount(self):
        self.tax_total = Decimal("0.08") * Decimal(self.sub_total)
        self.final_total = round((Decimal(self.sub_total) + Decimal(self.tax_total)), 2)
        return self.final_total

