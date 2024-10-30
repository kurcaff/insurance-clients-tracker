import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from insurances.models import Insurance

# KIRE: Models go here. This is data (like in a database). You define the schema of every table with this. 
# It shows which data we hold and the relationsip between the different data.

    


class Client(models.Model):

    # insurances = models.ManyToManyField(Insurance)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    insurances = models.ManyToManyField(Insurance, verbose_name="Insurances", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    birth_location = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    connection = models.CharField(max_length=100, blank=True, null=True)
    phone_home = models.CharField(max_length=20, blank=True, null=True)
    phone_mobile = models.CharField(max_length=20, blank=True, null=True)
    phone_work = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    employer = models.CharField(max_length=100, blank=True, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    customer_since = models.DateField(blank=True, null=True)
    bank_code = models.CharField(max_length=20, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    relationship_status = models.CharField(max_length=50, blank=True, null=True)
    partner_name = models.CharField(max_length=100, blank=True, null=True)
    partner_surname = models.CharField(max_length=100, blank=True, null=True)
    kids_number = models.PositiveIntegerField(blank=True, null=True)
    children_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Clients"
