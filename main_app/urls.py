from django.urls import path
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register_view, name='register'),


    # User trades and portfolio
    path('trades/', views.add_stock, name='add_stock'),
    path('watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('get_watchlist/', views.user_watchlist, name='user_watchlist'),
    path('view_trades/', views.users_stocks, name='users_stocks'),


    # Assets
    path('assets/search/<str:ticker>/', views.search_asset, name='search_asset'),
]
