import urllib.request, urllib.parse, urllib.error
import json
import ssl

def google() :
    api_key = False

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
        # This is free Geolocation API for educational purpose
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
        # This is the actual Google gerolocation API

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = input('Enter location: ')
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    index = url.find('&')

    print()
    print('Retrieving','........', url[29:index]+'.....')

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    #print('Place id',js['results'][0]['place_id'])
    #print(json.dumps(js, indent=4))
    #print(js)

    # print('City',js['results'][0]['address_components'][3]['long_name'])
    # print('State',js['results'][0]['address_components'][4]['long_name'])
    # print('Country',js['results'][0]['address_components'][5]['long_name'])
    # print('Pincode',js['results'][0]['address_components'][6]['long_name'])
    print('\n')
    print('Formatted Address :',js['results'][0]['formatted_address'])
    print('Lattitude :',js['results'][0]['geometry']['location']['lat'])
    print('Longitude :',js['results'][0]['geometry']['location']['lng'])
