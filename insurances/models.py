from django.db import models

# Create your models here.



class Insurance(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

# Chatgpt mi go dade ovoa bez da mu go potrazam
# class InsurancePolicy(models.Model):
#     policy_number = models.CharField(max_length=50)
#     coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
#     # Add any other fields specific to your insurance policy model

#     def __str__(self):
#         return self.policy_number

# Explanation:

# InsuranceCompany: This model represents an insurance company and includes
#  fields like name, street, zip code, place, phone number, email, 
# and website.

# InsurancePolicy: This model represents an insurance policy and includes 
# fields like policy number, coverage amount, start date, end date, 
# and a foreign key to link it to an insurance company. 
# You may add any other fields that are specific to your insurance policies.