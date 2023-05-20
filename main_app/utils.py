from bs4 import BeautifulSoup
import requests

def soup_data(ticker):
    response = requests.get(f'https://www.marketwatch.com/investing/stock/{ticker}')

    soup = BeautifulSoup(response.content, 'lxml')

    data = soup.find('bg-quote', attrs={'class': 'value'})
    co_name = soup.find('h1', attrs={'class': 'company__name'})

    
    data_parts = data.text
    data_part = data_parts.strip()

    current_stock = [co_name.text, data_part]
    return current_stock

def search_assets(ticker):
    response = requests.get(f'https://www.marketwatch.com/investing/stock/{ticker}')

    soup = BeautifulSoup(response.content, 'lxml')

    data = soup.find('bg-quote', attrs={'class': 'value'})
    co_name = soup.find('h1', attrs={'class': 'company__name'})

    data_parts = data.text
    data_part = data_parts.strip()

    asset_data = [co_name.text, data_part]
    return asset_data

def get_asset_price(ticker):
    response = requests.get(f'https://www.marketwatch.com/investing/stock/{ticker}')

    soup = BeautifulSoup(response.content, 'lxml')

    data = soup.find('bg-quote', attrs={'class': 'value'})
    
    data_parts = data.text
    data_part = data_parts.strip()

    return data_part
