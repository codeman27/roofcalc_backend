from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import re

def mortgage_rates(loan_type):
    url = 'https://www.nerdwallet.com/mortgages/mortgage-rates'
    pattern = r'(.*)%'
    pattern2 = r'(.*)-'

    request = urlopen(url)
    response = request.read()

    soup = BeautifulSoup(response, 'html.parser')

    table = soup.find('table')
    df = pd.read_html(str(table))[0]

    rate_data = {}
    rate_data['rate'] = float(re.search(pattern, df[df['Product'] == loan_type]['Interest rate'].values[0]).group(1))/100
    rate_data['years'] = float(re.search(pattern2, df[df['Product'] == loan_type]['Product'].values[0]).group(1))
    rate_data['loan_type'] = loan_type

    return rate_data

# print(mortgage_rates('30-year fixed rate'))
# print(mortgage_rates('15-year fixed rate'))
# print(mortgage_rates('5/1 ARM rate'))
#encode('utf-8')
#print(soup.encode('utf-8'))
