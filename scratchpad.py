class User(AbstractUser):
    zip_code = models.CharField(max_length=5)

    def get_portfolio(self):
        # Pseudo-code, not actual Django ORM code
        buys = self.trades.filter(trade_type='BUY').group_by('asset_type', 'ticker').sum('quantity')
        sells = self.trades.filter(trade_type='SELL').group_by('asset_type', 'ticker').sum('quantity')
        return buys - sells



# update Watchlist
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_to_watchlist(request, ticker):
    if request.method == "POST":
        if ticker not in request.user.watchlist:
            request.user.watchlist.append(ticker)
            request.user.save()
            return JsonResponse({"message": f"Added {ticker} to watchlist"}, status=201)
        else:
            return JsonResponse({"error": f"{ticker} is already in the watchlist"}, status=400)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def remove_from_watchlist(request, ticker):
    if request.method == "DELETE":
        if ticker in request.user.watchlist:
            request.user.watchlist.remove(ticker)
            request.user.save()
            return JsonResponse({"message": f"Removed {ticker} from watchlist"}, status=200)
        else:
            return JsonResponse({"error": f"{ticker} is not in the watchlist"}, status=400)
# add views to urls.py
path('watchlist/add/<str:ticker>/', views.add_to_watchlist, name='add_to_watchlist'),
path('watchlist/remove/<str:ticker>/', views.remove_from_watchlist, name='remove_from_watchlist'),
