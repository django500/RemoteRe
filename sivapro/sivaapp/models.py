from django.db import models
from multiselectfield import MultiSelectField
class ServicesData(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100,unique=True)
    course_duration = models.CharField(max_length=100)
    course_start_date = models.DateField(max_length=100)
    course_start_time = models.TimeField(max_length=100)
    course_trainer_name = models.CharField(max_length=100)
    course_trainer_exp =  models.CharField(max_length=100)
class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateField(max_length=100)
    feedback = models.CharField(max_length=500)
class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10)
    COURSES_CHOICES = (
        ('PY','PTHON'),
        ('DJ','DJANGO'),
        ('RA','REST API'),
        ('FL','FLASK'),
        ('J','JAVA'),
        ('UI','UI')
    )
    courses = MultiSelectField(choices=COURSES_CHOICES)
    SHIFTS_CHOISES = (
        ('Morning','Morning Shift'),
        ('Afternoon','Afternoon Shift'),
        ('Evening','Evening Shift'),
        ('Night','Night Shift')
    )
    shifts = MultiSelectField(choices=SHIFTS_CHOISES)
    start_date = models.DateTimeField(max_length=100)




