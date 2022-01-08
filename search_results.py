import requests
import xmltodict
import pandas as pd
from pandas.io.json import json_normalize
import api_keys

def search_results(address, city, state, zip):
    url = 'https://api.bridgedataoutput.com/api/v2/zestimates_v2/zestimates'
    params = {
        'access_token': api_keys.ZILLOW_API_KEY,
        'address': address, #self._loc.state
        'city': city,
        'state': state,
        'postalCode': zip
    }
    try:
        response = requests.get(url, params=params)
    except requests.ConnectionError:
        print('failed to connect')
        return

    df = pd.DataFrame.from_dict(response.json()['bundle'])
    print(address)
    df = df[df['address'].str.contains(address)][['address', 'zestimate', 'rentalZestimate']]
    print(df)
    zestimates = {}

    try:
        zestimates['zestimate'] = float(df['zestimate'])
        zestimates['rent_zestimate'] = float(df['rentalZestimate'])
    except:
        zestimates['zestimate'] = 0
        zestimates['rent_zestimate'] = 0

    return zestimates

from location import location
loc = location('519 Florida Ave, Clearwater FL 33756')
# loc = location('1810 E Palm Ave Apt 4208 Tampa, FL, 33605')
# address = loc['address'].replace(' ', '-')
# citystatezip = loc['city'] + '-' + loc['state'] +  '-'+ loc['zip']
print(loc)
# print(address)
# print(citystatezip)
print(search_results(loc['address'], loc['city'], loc['state'], loc['zip']))
