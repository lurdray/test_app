from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from transaction.models import * 
from transaction.serializers import *


from drf_yasg.utils import swagger_auto_schema


from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser 
  

@swagger_auto_schema(methods=['POST'], request_body=TransactionSerializer)
@api_view(['GET', 'POST'])
@csrf_exempt
def transaction_list(request): 
    """ 
    List all transaction, or create a new transaction 
    """
    if request.method == 'GET': 
        transaction = Transaction.objects.all() 
        serializer = TransactionSerializer(transaction, many=True) 
        return JsonResponse(serializer.data, safe=False) 
  
    elif request.method == 'POST': 
        data = JSONParser().parse(request) 
        serializer = TransactionSerializer(data=data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400) 
  
@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=TransactionSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def transaction_detail(request, pk): 
    try: 
        transaction = Transaction.objects.get(pk=pk) 
    except transaction.DoesNotExist: 
        return HttpResponse(status=404) 
  
    if request.method == 'GET': 
        serializer = TransactionSerializer(transaction) 
        return JsonResponse(serializer.data) 
  
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        serializer = TransactionSerializer(transaction, data=data) 
  
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=400) 
  
    elif request.method == 'DELETE': 
        transaction.delete() 
        return HttpResponse(status=204) 
    



@swagger_auto_schema(methods=['GET'], request_body=None)
@api_view(['GET'])
@csrf_exempt
def transaction_by_sender(request, sender, start, stop): 

    if sender: 
        transactions = Transaction.objects.filter(sender=sender).order_by('-pub_date')[int(start): int(stop)]
    else:
        transactions = Transaction.objects.all() 

    serializer = TransactionSerializer(transactions, many=True) 
    return JsonResponse(serializer.data, safe=False) 



@swagger_auto_schema(methods=['GET'], request_body=None)
@api_view(['GET'])
@csrf_exempt
def transaction_by_receiver(request, receiver, start, stop): 

    if receiver: 
        transactions = Transaction.objects.filter(receiver=receiver).order_by('-pub_date')[int(start): int(stop)]
    else:
        transactions = Transaction.objects.all() 

    serializer = TransactionSerializer(transactions, many=True) 
    return JsonResponse(serializer.data, safe=False) 