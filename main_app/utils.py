from bs4 import BeautifulSoup
import requests

def soup_data(ticker):
    response = requests.get(f'https://www.marketwatch.com/investing/stock/{ticker}')

    soup = BeautifulSoup(response.content, 'lxml')

    data = soup.find('bg-quote', attrs={'class': 'value'})
    co_name = soup.find('h1', attrs={'class': 'company__name'})
    extra = soup.find_all('li', attrs={'class': 'kv__item'})
    percentage = soup.find('span', attrs={'class': 'change--percent--q'})
    extra_data = []
    
    data_parts = data.text
    data_part = data_parts.strip()

    for info in extra:
        title, value = info.text.strip().split('\n', 1)
        extra_data.append({title: value})

    current_stock = [co_name.text, data_part]
    return [current_stock, extra_data, percentage.text]

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
