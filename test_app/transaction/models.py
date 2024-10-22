import uuid
from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    sender =  models.CharField(max_length=255, default=None)
    receiver =  models.CharField(max_length=255, default=None)
    amount =  models.FloatField(max_length=255, default=0)

    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.receiver


