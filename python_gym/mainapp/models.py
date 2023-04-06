from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, verbose_name="ID")
    URL = models.CharField(
        max_length=250, null=True, verbose_name="URL")
    Title = models.CharField(
        max_length=250, null=True, verbose_name="Title")
    Price = models.CharField(
        max_length=250, null=True, verbose_name="Price")
    Description = models.CharField(
        max_length=450, null=True, verbose_name="Description")
    DescriptionDetail = models.CharField(
        max_length=800, null=True, verbose_name="Description Detail")
    Category = models.CharField(
        max_length=250, null=True, verbose_name="Category")
    Quanity = models.IntegerField(
        null=True, verbose_name="Quanity")
    CreatedDate = models.DateTimeField(
        default=timezone.now, verbose_name="Created Date")

    def __str__(self):
        return f"{self.ID}"
class EmailWhiteList(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, verbose_name="ID")
    Description = models.CharField(
        max_length=200, null=True, verbose_name="Description")
    Email = models.CharField(
        max_length=200, null=True, verbose_name="Email")
    CreatedDate = models.DateTimeField(
        default=timezone.now, verbose_name="Created Date")
    def __str__(self):
        return f"{self.ID}"
