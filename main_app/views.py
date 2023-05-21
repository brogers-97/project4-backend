import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .utils import soup_data, search_assets, get_asset_price
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core import serializers
from .models import Trade, Follower

User = get_user_model()

@api_view(["GET"])
def scrape_soup_data(request, ticker):
    data = soup_data(ticker)
    return Response(data)


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = make_password(data.get("password"))  # hash the password
        zip_code = data.get("zip_code")

        user = User.objects.create(
            username=username, password=password, zip_code=zip_code
        )
        if user:
            return JsonResponse({"message": "User registered successfully"}, status=201)
        else:
            return JsonResponse({"error": "Unable to register user"}, status=400)


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "User logged in successfully"}, status=200)
        else:
            return JsonResponse({"error": "Invalid username or password"}, status=400)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == "GET":
        logout(request)
        return JsonResponse({"message": "User logged out successfully"}, status=200)


@csrf_exempt
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_trade(request):
    if request.method == "POST":
        data = json.loads(request.body)
        trade = Trade.objects.create(
            user=request.user,
            asset_type=data.get("asset_type"),
            ticker=data.get("ticker"),
            quantity=data.get("quantity"),
            price=data.get("price"),
            trade_type=data.get("trade_type"),
        )
        if trade:
            return JsonResponse({"message": "Trade created successfully"}, status=201)
        else:
            return JsonResponse({"error": "Unable to create trade"}, status=400)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_portfolio(request):
    if request.method == "GET":
        trades = Trade.objects.filter(user=request.user)
        portfolio = {}  # A dictionary to hold ticker and its total quantity
        for trade in trades:
            if trade.ticker in portfolio:
                if trade.trade_type == "BUY":
                    portfolio[trade.ticker] += trade.quantity
                else:  # trade_type is 'SELL'
                    portfolio[trade.ticker] -= trade.quantity
            else:
                portfolio[trade.ticker] = trade.quantity
        return JsonResponse(portfolio, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_users(request):
    if request.method == "GET":
        users = User.objects.all()
        users_json = serializers.serialize("json", users)
        return JsonResponse(users_json, safe=False)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def follow_user(request, username):
    if request.method == "POST":
        try:
            user_to_follow = User.objects.get(username=username)
            Follower.objects.create(user=request.user, followed_user=user_to_follow)
            return JsonResponse(
                {"message": f"Successfully followed {username}"}, status=201
            )
        except User.DoesNotExist:
            return JsonResponse(
                {"error": f"User {username} does not exist"}, status=400
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unfollow_user(request, username):
    if request.method == "DELETE":
        try:
            user_to_unfollow = User.objects.get(username=username)
            Follower.objects.get(
                user=request.user, followed_user=user_to_unfollow
            ).delete()
            return JsonResponse(
                {"message": f"Successfully unfollowed {username}"}, status=200
            )
        except User.DoesNotExist:
            return JsonResponse(
                {"error": f"User {username} does not exist"}, status=400
            )
        except Follower.DoesNotExist:
            return JsonResponse(
                {"error": f"You are not following {username}"}, status=400
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_portfolio(request, username):
    if request.method == "GET":
        try:
            user = User.objects.get(username=username)
            trades = Trade.objects.filter(user=user)
            portfolio = {}
            for trade in trades:
                if trade.ticker in portfolio:
                    if trade.trade_type == "BUY":
                        portfolio[trade.ticker] += trade.quantity
                    else:
                        portfolio[trade.ticker] -= trade.quantity
                else:
                    portfolio[trade.ticker] = trade.quantity
            return JsonResponse(portfolio, safe=False)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": f"User {username} does not exist"}, status=400
            )


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_trades(request, username):
    if request.method == "GET":
        try:
            user = User.objects.get(username=username)
            trades = Trade.objects.filter(user=user).values()
            return JsonResponse(list(trades), safe=False)
        except User.DoesNotExist:
            return JsonResponse(
                {"error": f"User {username} does not exist"}, status=400
            )


def search_asset(request, ticker):
    if request.method == "GET":
        try:
            assets = search_assets(ticker)
            return JsonResponse(assets, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


def get_asset_prices(request, ticker):
    if request.method == "GET":
        try:
            price = get_asset_price(ticker)
            return JsonResponse({"price": price})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
