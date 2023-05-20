from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    # path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),


    # User trades and portfolio
    # path('trades/', views.create_trade, name='create_trade'),
    # path('portfolio/', views.get_portfolio, name='get_portfolio'),

    # User interactions
    # path('users/', views.get_users, name='get_users'),
    # path('users/<str:username>/follow/', views.follow_user, name='follow_user'),
    # path('users/<str:username>/unfollow/', views.unfollow_user, name='unfollow_user'),
    # path('users/<str:username>/portfolio/', views.get_user_portfolio, name='get_user_portfolio'),
    # path('users/<str:username>/trades/', views.get_user_trades, name='get_user_trades'),

    # Assets
    # path('assets/search/<str:ticker>/', views.search_asset, name='search_asset'),
    # path('assets/prices/<str:ticker>/', views.get_asset_prices, name='get_asset_prices'),
]
