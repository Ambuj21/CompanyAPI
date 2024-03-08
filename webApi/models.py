from django.db import models


class Company(models.Model):
    options = (
        ('Tech', 'Computer'),
        ('Non Tech', 'Mobile Centre'),
        ('Non Tech', 'Call Centre'),
        ('Tech', 'Networking')
    )
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_location = models.CharField(max_length=100)
    company_type = models.CharField(max_length=50, choices=options)
    company_about = models.TextField(max_length=200)

    def __str__(self):
        return self.company_name + ' ' + self.company_location


#Employees


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    about = models.TextField(max_length=100)
    position = models.CharField(max_length=50, choices=(
        ('IT', 'Manager'),
        ('IT', 'Software Developer'),
        ('Non IT', 'Customer Care')
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
