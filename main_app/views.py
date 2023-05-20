from django.shortcuts import render
from django.http import HttpResponse
from .utils import soup_data
from rest_framework.response import Response 
from rest_framework.decorators import api_view

@api_view(['GET'])
def scrape_soup_data(request, ticker):
    data = soup_data(ticker)
    return Response(data)

def home(request):
  return HttpResponse('<h1>Welcome to SimuStock - home</h1>')