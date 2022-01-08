import api_keys
import requests
import geocoder

def location(address):
    try:
        result = geocoder.google(address, key=api_keys.GOOGLE_GEOCODE_API_KEY)
    except:
        print('failed to connect')
        return None

    location_parts = {}
    location_parts['address'] = (result.housenumber + ' ' + result.street)
    location_parts['city'] = result.city
    location_parts['state'] = result.state
    location_parts['zip'] = result.postal
    location_parts['county'] = str.strip((result.county).replace('County', '')) if result.county else result.city

    return location_parts
