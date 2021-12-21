import requests
import pandas as pd
import json
from datetime import datetime

pd.set_option('display.max_columns', None)

def data_usa(citystate):

    try:
        response = requests.get('https://datausa.io/api/search?dimension=Geography&hierarchy=Place&limit=50000')
    except:
        print('failed to connect to datausa')
        return

    df = pd.DataFrame.from_dict(response.json()['results'])
    data_id = df[(df['name'] == citystate) & (df['hierarchy'] == 'Place')]['id']  #Added Place. Without that then places will return multiple IDs which breaks the API.

    if data_id.empty:
        data_id = df[df['name'] == citystate.replace('St', 'St.')]['id'] #Not sure how to handle this... St. Pete Beach vs St Pete Beach, Geolocation doesn't give Census ID for some reason

    measure_names = ['Household Income by Race', 'Population', 'Workforce by Occupation and Gender']
    measures = {}

    print(data_id)
    print(measure_names)
    for measure in measure_names:
        url = 'http://datausa.io/api/data'
        params = {
            'Geography': data_id,
            'measure': measure,
        }
        try:
            response = requests.get(url, params=params, timeout=5)
            print(response.url)
        except requests.ConnectionError:
            print('failed to connect to datausa')
            return

        df = pd.DataFrame(response.json()['data'])
        df['pct_change'] = df[measure].pct_change(-1)
        measure_change = df['pct_change'].mean()
        recent_measure = df[df['Year'] == df['Year'].max()][measure][0]
        pred_measure = recent_measure * pow(1 + measure_change, int(datetime.now().year) - int(df['Year'].max()))

        measures[measure] = round(pred_measure)
        measures[measure + '_Change'] = round(measure_change, 4)

    return measures

from location import location

loc = location('519 Florida Ave, Clearwater, FL 33756')
#loc = location('146 Robin Ln, Panama City Beach, FL 32407')
address = loc['address'].replace(' ', '-')
citystate = loc['city'] + ', ' + loc['state']
print(address)
print(citystate)
print(data_usa(citystate.replace('-' , ', ')))
