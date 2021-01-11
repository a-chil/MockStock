from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


class Stock(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null="True")
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    price_per_stock = models.FloatField()
    shares = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol

    class Meta:
        ordering = ["-purchase_date"]
