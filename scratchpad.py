class User(AbstractUser):
    zip_code = models.CharField(max_length=5)

    def get_portfolio(self):
        # Pseudo-code, not actual Django ORM code
        buys = self.trades.filter(trade_type='BUY').group_by('asset_type', 'ticker').sum('quantity')
        sells = self.trades.filter(trade_type='SELL').group_by('asset_type', 'ticker').sum('quantity')
        return buys - sells
