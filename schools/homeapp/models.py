from django.db import models
from datetime import datetime

from random import randint


def random_with_N_digit(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Create your models here.
STATUS_CHOICES=[
        (True,'Sent email'),
        (False,'Not Send'),
    ]

class Registration(models.Model):
    your_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    nid_number = models.IntegerField()
    present_address = models.TextField()
    parmanent_address = models.TextField()
    passing_year = models.CharField(max_length=100)
    dob = models.DateField()
    blood_group = models.CharField(max_length=5)
    occupation = models.CharField(max_length=100)
    batchmate_name = models.CharField(max_length=100)
    batchmate_phone_number = models.CharField(max_length=20)
    your_phone_number = models.CharField(max_length=20)
    your_email = models.EmailField()
    status = models.BooleanField(default=False,choices=STATUS_CHOICES)
    event = models.ForeignKey("Event", on_delete=models.CASCADE,null=True)


class Event(models.Model):
    title    =models.CharField(max_length=50)
    description  = models.TextField(null=True)
    event_time   =models.DateField(auto_now=True, auto_now_add=False)
    created_at   =models.DateField(auto_now=True, auto_now_add=False)
    status      =models.BooleanField(default=True)

    def __str__(self):
        return self.title

def __self__(self):
    return self.name

def get_absolute_url(self):
    return reverse("homeapp:home")



# for event registrations 

class EventMemberRegistration(models.Model):
    your_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    dob = models.DateField()
    blood_group = models.CharField(max_length=5)
    occupation = models.CharField(max_length=100)
    occupation_designation =models.CharField(max_length=100)
    present_address = models.TextField()
    your_phone_number = models.CharField(max_length=20)
    your_email = models.EmailField()
    parmanent_address = models.TextField()
    passing_year = models.CharField(max_length=100)
    your_phone_number = models.CharField(max_length=20)
    transaction_number = models.IntegerField();
    
    status = models.BooleanField(default=False,choices=STATUS_CHOICES)
    event = models.ForeignKey("Event", on_delete=models.CASCADE,null=True)


