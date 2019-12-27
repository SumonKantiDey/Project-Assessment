from apscheduler.schedulers.background import BackgroundScheduler
from scheduleUpdater import ttlset
from api.models import Store 
#from datetime import datetime, timedelta
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(ttlset.remove_data, 'interval', minutes=1)
    scheduler.start()