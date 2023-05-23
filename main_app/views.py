import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .utils import soup_data
from rest_framework.response import Response
from rest_framework.decorators import (api_view)
from .models import Trade

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

            refresh = RefreshToken.for_user(user)
            res_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'User got in'
            }

            return JsonResponse(res_data, status=201)
        else:
            return JsonResponse({"error": "Unable to register user"}, status=400)

@csrf_exempt
def search_asset(request, ticker):
    if request.method == "GET":
        try:
            # assets = search_assets(ticker)
            assets = soup_data(ticker)
            return JsonResponse(assets, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

def users_stocks(request):
    if request.method == 'GET':
        try:
            stocks = Trade.objects.all().values()
            return JsonResponse(list(stocks), safe=False)
        except Trade.DoesNotExist:
            return JsonResponse({"message": "User stocks not found"}, status=404)

@csrf_exempt
def trade_stock(request):
    if request.method == 'POST':
        try:
            print(request.body)
            data = json.loads(request.body)

            new_trade = Trade(
                asset_type=data['asset_type'],
                ticker=data['ticker'],
                quantity=data['quantity'],
                price=data['price'],
                trade_type=data['trade_type'],
                user_id=data['user_id']
            )

            new_trade.save()

            return JsonResponse({"message": "Trade added successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)

@csrf_exempt
def add_to_watchlist(request):
    if request.method == 'POST':
        try:
            print(request.body)
            data = json.loads(request.body)
            print(data)
            user_id = data.get('user_id')
            new_stock = data.get('new_stock')
            user = User.objects.get(id=user_id)

            if user.watchlist is None:
                user.watchlist = {}

            user.watchlist.append(new_stock)
            user.save()

            return JsonResponse({"message": "Stock added successfully"}, status=201)
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)

def user_watchlist(request):
    if request.method == 'GET':
        try:
            
            user_id = request.GET.get('user_id')
            user = User.objects.get(id=user_id)
            watchlist = user.watchlist
            print(watchlist)

            return JsonResponse(watchlist, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)

def get_user(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            print(user_id)
            user = User.objects.get(id=user_id)
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'funds': user.funds
            }
            return JsonResponse(user_data, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)