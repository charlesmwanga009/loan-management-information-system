from django.db import models

from django.core.exceptions import ValidationError
import math

Departmentlist=(
    ('mainoffice','mainoffice'),
    ('market and public relationship','market and public relationship'),
    ('customer services','customer services'),
    ('finance','finance'),
    ('ict','ict'),

)
HODlist=(
    ('manager_director','manager_director'),
    ('diputy_director','diputy_director'),
    ('head of marketing department','head of marketing department'),
    ('head of customer service','head of customer service'),
    ('head of finance department','head of finance departmen'),
    ('head of HR department','head of HR department'),
    ('head of ict','head od ict'),
)
brancheslist=(
    ('main branch','main branch'),
    ('kilimanjaro branch','kilimanjaro branch'),
    ('arusha','arusha'),
    ('manyara','manyara'),

)
Region=(
    ('kilimajanro','kilimanjaro'),
    ('manyara','manyara'),
    ('arusha','arusha'),
)
sponserList=(
    ('sponser1','sponser1'),
    ('sponser2','sponser2'),
    ('sponser3','sponser3'),
)
amount=(
    ('50000-1000000 Tsh','50000-100000 Tsh'),
    ('150000-2000000 Tsh','150000-200000 Tsh'),
    ('250000-3000000 Tsh','250000-300000 Tsh'),
    ('350000-4000000 Tsh','350000-400000 Tsh'),
    ('450000-5000000 Tsh','450000-500000 Tsh'),
    ('550000-6000000 Tsh','550000-600000 Tsh'),
    ('650000-7000000 Tsh','650000-700000 Tsh'),
    ('700000-1000000 Tsh','700000-1000000 Tsh'),
)
Loan_typelist=(
    ('education loan','education loan'),
    ('bulding loan','bulding loan'),
    ('home loan','home loan'),
    ('busness loan','busness loan'),
)
class Department(models.Model):
    department_name=models.CharField(max_length=200,primary_key=True,choices=Departmentlist)
     
      
class HOD(models.Model):
    HOD_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,primary_key=True)
    age=models.IntegerField()
    date_registered=models.DateField(auto_now_add=True)
    branches=models.CharField(max_length=200,choices=brancheslist)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.HOD_name
     

class  customer(models.Model):
     full_name = models.CharField(max_length=255)
     email=models.CharField(max_length=200,primary_key=True)
     purpose_of_loan=models.CharField(max_length=600)
     age=models.IntegerField()
     amount=models.IntegerField()
     Loan_typelist=models.CharField(max_length=200,choices=Loan_typelist)
     Region=models.CharField(max_length=200,choices=Region)
     image=models.ImageField(upload_to='customer/')
     date_registered=models.DateField(auto_now_add=True)
     branches=models.CharField(max_length=200,choices=brancheslist)
     department=models.ForeignKey(Department,on_delete=models.CASCADE)
     def __str__(self):
             return self.email
     def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.image.url))


class  sponser(models.Model):
     full_name=models.CharField(max_length=200,primary_key=True)
     email=models.CharField(max_length=200)
     sponsernumber=models.CharField(max_length=200,choices=sponserList)
     age=models.IntegerField()
     Region=models.CharField(max_length=200,choices=Region)
     image=models.ImageField(upload_to='sponser/')
     date_registered=models.DateField(auto_now_add=True)
     
     department=models.ForeignKey(Department,on_delete=models.CASCADE)
     def __str__(self):
             return self.full_name
     def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.image.url))

class branches(models.Model):
    branch_name=models.CharField(max_length=200,primary_key=True,choices=brancheslist)
class  staff(models.Model):
     staff_name=models.CharField(max_length=200)
     email=models.CharField(max_length=200,primary_key=True)
     age=models.IntegerField()
     image=models.ImageField(upload_to='staff/')
     date_registered=models.DateField(auto_now_add=True)
     branches=models.CharField(max_length=200,choices=brancheslist)
     department=models.ForeignKey(Department,on_delete=models.CASCADE)
     def __str__(self):
             return self.staff_name
     def image_tag(self):
            return mark_safe('<img src="%s"width="50"style="border-radius:4px">'% (self.image.url))


class Announcements(models.Model):
     heading=models.CharField(max_length=200)
     title=models.CharField(max_length=200)
     date_registered=models.DateField(auto_now_add=True)
     file=models.FileField(upload_to='announcements/')
     def __str__(self):
             return self.title

class LoanApplication(models.Model):
    customer_name = models.CharField(max_length=255,primary_key=True)
    loan_amount = models.IntegerField()  # Loan amount must be an integer (no decimal values)
    loan_period_months = models.IntegerField()  # Loan period in months (integer)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2, default=10.2)  # Fixed interest rate (10.2%)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Total repayment with decimal values
    daily_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Daily repayment with decimals
    weekly_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Weekly repayment with decimals
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Monthly repayment with decimals

    def clean(self):
        # Ensure loan amount and loan period are valid
        if self.loan_amount <= 0:
            raise ValidationError("Loan amount must be greater than zero.")
        if self.loan_period_months <= 0:
            raise ValidationError("Loan period must be at least one month.")

    def calculate_total_payment(self):
        """
        Formula: Total Payment = Loan Amount + (Loan Amount * Interest Rate * Loan Period in years)
        Interest rate is fixed at 10.2%.
        The result will be rounded to two decimal places for accurate currency representation.
        """
        interest_decimal = self.interest_rate / 100
        # Calculate total interest based on the loan period in years
        total_interest = self.loan_amount * interest_decimal * (self.loan_period_months)
        # Return total repayment rounded to two decimal places
        return round(self.loan_amount + total_interest)

    def calculate_payments(self):
        """
        Calculate daily, weekly, and monthly repayment amounts with two decimal places.
        """
        # Calculate total payment
        total_payment = self.calculate_total_payment()

        # Calculate monthly payment by dividing the total payment by the loan period in months
        self.monthly_payment = round(total_payment / self.loan_period_months)

        # Calculate weekly payment assuming 4.33 weeks per month
        self.weekly_payment = round(self.monthly_payment / 4.33)

        # Calculate daily payment assuming 30 days per month
        self.daily_payment = round(self.monthly_payment / 30)

    def save(self, *args, **kwargs):
        # Before saving, calculate total payment and installment payments
        self.total_payment = self.calculate_total_payment()
        self.calculate_payments()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer_name} - {self.loan_amount}'

