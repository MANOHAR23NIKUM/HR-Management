from django.db import models

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
     