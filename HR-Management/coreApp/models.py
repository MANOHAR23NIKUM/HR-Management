from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Leave(models.Model):
    LEAVE_TYPES = [
        ('Sick', 'Sick Leave'),
        ('Casual', 'Casual Leave'),
        ('Paid', 'Paid Leave'),
        ('Unpaid', 'Unpaid Leave'),
    ]

    LEAVE_STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    leave_id = models.IntegerField()
    leave_type = models.CharField(max_length=100, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=LEAVE_STATUS, default='Pending')


# Create your models here.

    # class User(models.Model):
    #     USER_GENDER = [
    #         ('Male','Male'),
    #         ('Female','Female')
    #     ]

    #     username = models.CharField(max_length=50)
    #     first_name = models.CharField(max_length=50)
    #     last_name= models.CharField(max_length=50)
    #     email = models.EmailField()
    #     gender = models.CharField(max_length=50 , choices=USER_GENDER)
    #     contact = models.CharField(max_length=50)
    #     date_of_join = models.DateField(null=True)
    

class Attendance(models.Model):
    ATTENDANCE = [
        ('Present','Present'),
        ('Absent','Absent')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    log_in = models.TimeField(blank=True)
    log_out = models.TimeField(blank=True)
    status = models.CharField(max_length=50,choices=ATTENDANCE) 
     