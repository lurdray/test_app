from rest_framework import serializers
from transaction.models import *



###################
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"




###############



class CreateTransactionSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=150)
    receiver = serializers.CharField(max_length=150)
    amount = serializers.CharField(max_length=150)

