from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Items(models.Model):
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name