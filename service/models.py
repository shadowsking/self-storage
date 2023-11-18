from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tg_nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class TypeStorage(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Storage(models.Model):
    type_storage = models.ForeignKey(TypeStorage, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_storage.name


class Order(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    date_at = models.DateField()
    date_to = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user
