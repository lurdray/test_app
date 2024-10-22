from django.contrib import admin
from custom_user.models import CustomUser
from transaction.models import Transaction


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Transaction)
