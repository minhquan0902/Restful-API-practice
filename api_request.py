import httplib2
import json


def getGeocodeLocation():
    google_api_key = input("Input yopur google api key here: ")
    inputString = input("Input your search Query: ")
    locationString = inputString.replace(" ","+")
    url = ("https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longtitude = result['results'][0]['geometry']['location']['lng']
    print("response header: {} \n \n".format(response))
    print(result)
    print('\n')
    print(latitude)
    print(longtitude)



getGeocodeLocation()