from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True) #blank =True => Optional
    created_at = models.DateTimeField(auto_now_add=True) #Used for new insertion
    modified_at = models.DateTimeField(auto_now=True) #Used for the update

    def __str__(self):
        return self.first_name #It will be the employee identifier in the database, but not the pk(employee.id)