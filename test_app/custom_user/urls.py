from django.urls import path
from custom_user.views import *

app_name = "custom_user"

urlpatterns = [
    path('sign-up/', sign_up, name='sign_up'),
    path('sign-in/', sign_in, name='sign_in'),
    path('all/', all, name='all'),
    path('update/<str:user_id>/', update_user, name='update_user'),
    path('delete/<str:user_id>/', delete_user, name='delete_user'),
    path('get-user-detail/<str:user_id>/', get_user_detail, name='get_user_detail'),

    path('initiate-transfer/<str:pk>/', add_transaction_to_user, name = 'add_transaction_to_user'), 
    path('get-user-detail/<str:user_id>/balance/', get_balance, name='get_balance'),

    

    

    
]
