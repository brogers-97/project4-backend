from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    zip_code = models.CharField(max_length=5)
    objects = UserManager()

ASSET_TYPES = [
    ('STOCK', 'Stock'),
    ('CRYPTO', 'Crypto'),
]

TRADE_TYPES = [
    ('BUY', 'Buy'),
    ('SELL', 'Sell'),
]

class Trade(models.Model):
    user = models.ForeignKey(User, related_name='trades', on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES)  # "Stock" or "Crypto"
    ticker = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)  # "BUY" or "SELL"
    timestamp = models.DateTimeField(auto_now_add=True)

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user')
