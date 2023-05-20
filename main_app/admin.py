from django.contrib import admin
from .models import User, Trade, Follower

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'zip_code']
    
class TradeAdmin(admin.ModelAdmin):
    list_display = ['user', 'asset_type', 'ticker', 'quantity', 'price', 'trade_type', 'timestamp']

class FollowerAdmin(admin.ModelAdmin):
    list_display = ['user', 'followed_user', 'timestamp']

admin.site.register(User, UserAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(Follower, FollowerAdmin)
