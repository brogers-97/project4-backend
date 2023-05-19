from django.shortcuts import render
from .utils import soup_data
from rest_framework.response import Response 
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def scrape_soup_data(request, ticker):
    data = soup_data(ticker)
    return Response(data)