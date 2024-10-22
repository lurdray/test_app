
from django.urls import path 
from . import views 

app_name = "transaction"

urlpatterns = [

    path('transaction/', views.transaction_list, name = 'ptransaction_list'), 
    path('transaction/<str:pk>/', views.transaction_detail, name = 'transaction_detail'),

    path('filter/transaction/<str:sender>/by-sender/<int:start>/<int:stop>/', views.transaction_by_sender, name = 'transaction_by_sender'),
    path('filter/transaction/<str:receiver>/by-receiver/<int:start>/<int:stop>/', views.transaction_by_receiver, name = 'transaction_by_receiver'),

    

]

