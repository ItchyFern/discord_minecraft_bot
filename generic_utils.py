from urllib.request import urlopen
from json import loads

def get_dict(url):
    data_json = loads(get_response(url))
    return data_json

def get_response(url):
    #print(url)
    response = urlopen(url)
    return response.read()