from django.core.management.base import BaseCommand
from django.utils import timezone

from users.models import Employess

import requests
import datetime


class Command(BaseCommand):
    help = 'Download employees data from realmdigital api and save it on database.'

    def get_data(self):
        result_list = {}
        response = requests.get("https://interview-assessment-1.realmdigital.co.za/employees")
        result_list = response.json()

        return result_list

    def convert_datetime(self, date_to_convert):
        #convert iso format datetime into date

        try:
            if(date_to_convert is None):
                pass
            new_datetime = datetime.datetime.fromisoformat(str(date_to_convert))
            return str(new_datetime)[:10]
        except ValueError: 
            pass

    
    def notification(self, data):
        #convert notifications dates into readable dates

        last_notification = ''
        last_birthday_notified = ''
        try:
            last_notification = data['lastNotification'][:10]
            last_birthday_notified = data['lastBirthdayNotified'][:10]
            return last_notification, last_birthday_notified
        except TypeError:
            pass

    
    def handle(self, *args, **kwargs):
        json_data = self.get_data()
        last_notification = None
        last_birthday_notified = None

        for data in json_data:
            try:
                email = f"{data['name']}{data['lastname']}@realmdigital.co.za"
                date_of_birth=self.convert_datetime(data['dateOfBirth'])
                employment_start_date=self.convert_datetime(data['employmentStartDate'])
                employment_end_date=self.convert_datetime(data['employmentEndDate'])

                if "lastNotification" not in data or "lastBirthdayNotified" not in data:
                    last_notification = None
                    last_birthday_notified = None
                else:
                    last_notification, last_birthday_notified = self.notification(data)

                Employess.objects.create(
                    email=email, 
                    name=data['name'],
                    last_name=data['lastname'],
                    date_of_birth=date_of_birth,
                    employment_start_date=employment_start_date,
                    employment_end_date=employment_end_date,
                    last_birthday_notified=last_birthday_notified,
                    last_notification=last_notification
                )
            except KeyError:
                pass
