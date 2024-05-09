from django.db import models
from datetime import datetime


class postt(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=10000000)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
