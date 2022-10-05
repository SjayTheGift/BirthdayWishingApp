from django.core.management.base import BaseCommand
from django.utils import timezone
import requests

class Command(BaseCommand):
    help = 'Download employees data from realmdigital api and save it on database.'

    def get_data(self):
        # result_list = {}
        response = requests.get("https://interview-assessment-1.realmdigital.co.za/employees")
        result_list = response.json()['results']

        return result_list

    def handle(self, *args, **kwargs):
        json_data = self.get_data()

        print(json_data)
        # self.stdout.write("It's now %s" % time)