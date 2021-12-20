from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import re

def property_taxes(state, county, house_price):
    url = 'https://smartasset.com/taxes/' + state +'-property-tax-calculator'
    pattern = r'(.*)%'
    pattern2 = r'(.*)/s'

    request = urlopen(url)
    response = request.read()

    soup = BeautifulSoup(response, 'html.parser')

    table = soup.findAll('table')[6]
    df = pd.read_html(str(table))[0]

    tax_data = {}
    tax_data['tax_rate'] = round(float(re.search(pattern, df[df['County'] == county + ' County']['Average Effective Property Tax Rate'].values[0]).group(1))/100, 4)
    tax_data['tax_amt_yr'] = round(tax_data['tax_rate'] * house_price)
    tax_data['tax_amt_mn'] = round(tax_data['tax_rate'] * house_price/12)

    return tax_data

# print(property_taxes('mo', 'Adair', 185900))
