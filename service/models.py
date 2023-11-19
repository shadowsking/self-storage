from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User


class TypeStorage(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        "Номер телефона",
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=255)
    type_storage = models.ForeignKey(TypeStorage, on_delete=models.CASCADE, related_name="storages")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="storages")

    def __str__(self):
        return self.type_storage.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name="orders")
    date_at = models.DateField(default=timezone.now)
    date_to = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.email
