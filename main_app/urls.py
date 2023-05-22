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
    path('trades/', views.create_trade, name='create_trade'),


    # Assets
    path('assets/search/<str:ticker>/', views.search_asset, name='search_asset'),
]
