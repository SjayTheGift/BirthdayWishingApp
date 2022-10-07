from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError

from users.models import Employess

def send_emploee_birthday():
    today = timezone.now().date()
    for user in Employess.objects.filter(
        date_of_birth__day=today.day, 
        date_of_birth__month=today.month, 
        employment_start_date__lte=today,
        employment_start_date__isnull=False):
        
        if(user.employment_end_date == None or user.employment_end_date >= today):
            if(user.last_notification != today and user.last_birthday_notified != today):
                print('send email')

                subject = f'Happy Birthday {user.name} {user.last_name}'
                body = f'Happy Birthday {user.name} {user.last_name} from the realm digital team.'
                try:
                    send_mail(subject, body, 'contact@reamldigital.co.za', [user.email],  fail_silently=False,)
                except BadHeaderError:
                    pass
            
                print(f'{user.name} {user.last_name} email sent with birthday wish')

                print(user.pk)

                Employess.objects.filter(pk=user.pk).update(last_notification=today, last_birthday_notified=today)


