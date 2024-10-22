import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone
from transaction.models import Transaction



    
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transactions = models.ManyToManyField(Transaction, through="CustomUserTransactionConnector", blank=True)

    balance =  models.FloatField(max_length=255, default=0)
    
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)
	
    def __str__(self) -> str:
        return self.username


class CustomUserTransactionConnector(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)



