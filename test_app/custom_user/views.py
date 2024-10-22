from django.contrib.auth import get_user_model, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema

from custom_user.models import *
from custom_user.serializers import *

from transaction.serializers import *
from transaction.models import *

from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser 





@swagger_auto_schema(method='post', request_body=SignUpSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        email = serializer.validated_data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'id': user.id}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=SignInSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'id': user.id}, status=status.HTTP_200_OK)



@swagger_auto_schema(method='get', responses={200: UserSerializer(many=True)})
@api_view(['GET'])
@permission_classes([AllowAny])
def all(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




# test_app/custom_user/views.py
@swagger_auto_schema(method='put', request_body=UpdateUserSerializer, responses={200: UpdateUserSerializer()})
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')

    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.save()

    return Response({'msg': "User updated!", 'id': user.id}, status=status.HTTP_200_OK)


@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@swagger_auto_schema(method='get', responses={200: UserSerializer()})
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)




@swagger_auto_schema(methods=['POST'], request_body=TransactionSerializer)
@api_view(['POST',])
@csrf_exempt
def add_transaction_to_user(request, pk): 
    #serializer = UpdatebillingSerializer(data=request.data)
    try: 
        custom_user = CustomUser.objects.get(id=pk) 
    except CustomUser.DoesNotExist: 
        return HttpResponse(status=404) 
    
    print(1)
    
    sender = request.data.get('sender')
    receiver = request.data.get('receiver')
    amount = request.data.get('amount')

    try: 
        custom_user1 = CustomUser.objects.get(username=sender) 
    except CustomUser.DoesNotExist: 
        return Response({'error': 'Sender not found'}, status=status.HTTP_404_NOT_FOUND)


    #check if receiver exist
    try: 
        custom_user2 = CustomUser.objects.get(username=receiver) 
    except CustomUser.DoesNotExist: 
        return Response({'error': 'Receiver not found'}, status=status.HTTP_404_NOT_FOUND)
    
    print(2)

    #check if balance is up 2 amount
    if float(custom_user.balance) >= float(amount):
        pass
    else:
        return Response({'error': 'Insufficient funds'}, status=status.HTTP_404_NOT_FOUND)
    
    print(3)
        
    #send
    custom_user.balance -= float(amount)
    custom_user.save()

    custom_user2.balance += float(amount)
    custom_user2.save()

    print(4)


    transaction = Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)
    transaction.save()

    ct = CustomUserTransactionConnector(user=custom_user, transaction=transaction)
    ct.save()

    ct = CustomUserTransactionConnector(user=custom_user2, transaction=transaction)
    ct.save()


    return Response({'status': "Transfer successful!", "sender": sender, "receiver": receiver, "amount": amount, "balance": custom_user.balance}, status=status.HTTP_200_OK)



@swagger_auto_schema(method='get', responses={200: UserSerializer()})
@api_view(['GET'])
@permission_classes([AllowAny])
def get_balance(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'balance': user.balance}, status=status.HTTP_200_OK)

