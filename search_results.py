import requests
import xmltodict
import pandas as pd
from pandas.io.json import json_normalize
import api_keys

def search_results(address, citystatezip):
    url = 'https://www.zillow.com/webservice/GetSearchResults.htm'
    params = {
        'zws-id': api_keys.ZILLOW_API_KEY,
        'address': address, #self._loc.state
        'citystatezip': citystatezip,
        'rentzestimate': True
    }
    try:
        result = requests.get(url, params=params)
    except requests.ConnectionError:
        print('failed to connect')
        return

    zestimates = {}

    try:
        dict = xmltodict.parse(result.content)
    except:
        zestimates['zestimate'] = 0
        zestimates['rent_zestimate'] = 0
        print('Error zillow parsing xml')
        return zestimates

    df = pd.DataFrame.from_records(dict['SearchResults:searchresults']['response']['results']['result'])

    try:
        zestimates['zestimate'] = float(df['zestimate']['amount']['#text'])
        zestimates['rent_zestimate'] = float(df['rentzestimate']['amount']['#text'])
    except:
        zestimates['zestimate'] = 0
        zestimates['rent_zestimate'] = 0

    return zestimates

# from location import location
# loc = location('5018 Miami St, St. Louis, MO 63139')
# loc = location('1810 E Palm Ave Apt 4208 Tampa, FL, 33605')
# address = loc['address'].replace(' ', '-')
# citystatezip = loc['city'] + '-' + loc['state'] +  '-'+ loc['zip']
# print(address)
# print(citystatezip)
# print(search_results(address, citystatezip))
