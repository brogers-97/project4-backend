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