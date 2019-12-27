import time
from datetime import datetime,timedelta
from api.models import Store
def remove_data():
    print("Hello")
    Store.objects.filter(posting_date__lte=datetime.now()-timedelta(minutes=5)).delete()