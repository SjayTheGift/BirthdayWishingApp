from django.db import models


# class LastBirthDayNotification(models.Model):
#     last_birthday_notified = models.DateField(blank=True, null=True)


# class LastNotification(models.Model):
#     last_notification = models.DateField(blank=True, null=True)


class Employess(models.Model):
    email = models.EmailField(max_length=150)
    name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField()
    employment_start_date = models.DateField()
    employment_end_date = models.DateField(blank=True, null=True)    
    last_birthday_notified = models.DateField(blank=True, null=True)
    last_notification = models.DateField(blank=True, null=True)


