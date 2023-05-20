from django.shortcuts import render
from django.http import HttpResponse
from .utils import soup_data
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
import json

@api_view(['GET'])
def scrape_soup_data(request, ticker):
    data = soup_data(ticker)
    return Response(data)

def home(request):
  return HttpResponse('<h1>Welcome to SimuStock - home</h1>')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return 'invalid login'

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('userEmail')
        password = data.get('userPassword')
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'invalid request method'}, status=status.HTTP_400_BAD_REQUEST)