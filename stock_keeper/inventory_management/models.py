from django.contrib.auth.models import User
from django.db import models


class StorageLocation(models.Model):
    name = models.CharField(max_length = 255, blank = False)
    max_weight_capacity = models.IntegerField(blank = False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Shelf(models.Model):
    location = models.ForeignKey(StorageLocation, on_delete = models.CASCADE, related_name = 'storage_location')
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'product_on_shelf')
    current_quantity = models.IntegerField(default = 100)

    def __str__(self):
        return f'{self.location.name} - {self.product.name}'


class InventoryManagementTask(models.Model):
    TASK_STATUS_CHOICES = (
        ("WAITING", "waiting"),
        ("PARSING", "parsing"),
        ("OK", "ok"),
    )

    task_status = models.CharField(
        choices = TASK_STATUS_CHOICES,
        default = 'WAITING',
        max_length = 30,
    )
    user = models.ForeignKey(User, related_name = 'user_inventory_management_tasks', on_delete = models.CASCADE)
    result = models.JSONField(default = dict)
