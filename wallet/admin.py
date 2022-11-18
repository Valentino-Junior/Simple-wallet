from django.contrib import admin
from .models import Wallet

class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance')
    list_filter = ('user',)

admin.site.register(Wallet, WalletAdmin)
