from django.db import models
from datetime import datetime 
# Create your models here.


class Store(models.Model):
    key = models.CharField(max_length=256)
    value = models.TextField() 
    posting_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.value

    class Meta:
        db_table = "store"
