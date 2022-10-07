from apscheduler.schedulers.background import BackgroundScheduler
from .views import send_emploee_birthday


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_emploee_birthday, 'cron', minute='*/1')
    scheduler.start()