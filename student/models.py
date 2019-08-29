from django.db import models
from datetime import *
from django.urls import reverse
from django.utils import timezone
from django.core.validators import RegexValidator

#Choices


BELT_COLOR = (
    ('White', 'White'),
    ('Yellow', 'Yellow'),
    ('Yellow Black', 'Yellow Black'),
    ('Green', 'Green'),
    ('Green Black', 'Green Black'),
    ('Purple', 'Purple'),
    ('Purple Black', 'Purple Black'),
    ('Orange', 'Orange'),
    ('Orange Black', 'Orange Black'),
    ('Blue', 'Blue'),
    ('Blue Black', 'Blue Black'),
    ('Brown', 'Brown'),
    ('Brown Black', 'Brown Black'),
    ('Red', 'Red'),
    ('Red Black', 'Red Black'),
    ('Black', 'Black')
)

#Global Constants
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)



class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100, default="NA")
    city = models.CharField(max_length=100, default="NA")
    province = models.CharField(max_length=100, default="NA")
    postal_code = models.CharField(max_length=10, default="NA")
    email_ID = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def address(self):
        return self.street_name + " " + self.city + " " + self.province

    def __str__(self):
        return self.last_name



class Guardian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100, default="NA")
    city = models.CharField(max_length=100, default="NA")
    province = models.CharField(max_length=100, default="NA")
    postal_code = models.CharField(max_length=10, default="NA")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
  

    def address(self):
        return self.street_name + ", " + self.city + ", " + self.province

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('student:student')

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100, default="NA")
    city = models.CharField(max_length=100, default="NA")
    province = models.CharField(max_length=100, default="NA")
    postal_code = models.CharField(max_length=10, default="NA")
    date_of_birth = models.DateField()
    date_of_joining = models.DateField(default=timezone.now)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    rank = models.CharField(max_length=50, choices=BELT_COLOR, default='White')
    guardian = models.ForeignKey(Guardian, null=True, blank=True, on_delete=models.SET_NULL, related_name='children')

    def address(self):
        return self.street_name + " " + self.city + " " + self.province

    def get_absolute_url(self):
        return reverse('student:student')

    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self):
        return self.first_name +" " + self.last_name


class Attendance(models.Model):
    attendance_date = models.DateField(max_length=20, default=timezone.now)
    attendance_count = models.IntegerField(default=1)
    student = models.ForeignKey(Student,null=True, blank=True, on_delete=models.CASCADE, related_name='attendances')

    def __str__(self):
        return str(self.attendance_count)

    def get_absolute_url(self):
        return reverse('student:attend')



